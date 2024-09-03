---
title: Roughly Everything You Need to Know About Entity Resolution
main_image: nyc2018/63.jpg
layout: post
category: articles
tags: [data, machine learning, technology, software engineering, programming]
description: Naming things is hard. This is not just a technical problem, but a foundational problem that we have as humans when we talk to each other and refer to specific things and people. I have four good friends named Zach – there's a reason we invented nicknames. Leaning on my experience designing the data pipelines that created and maintained Vouch's knowledge graph of the startup ecosystem, in this blog post, I'll discuss some of the key ideas behind ER systems, and the challenges in building them.

---

Naming things is hard. This is not just a technical problem, but a foundational problem that we have as humans when we talk to each other and refer to specific things and people. I have four good friends named Zach – there's a reason we invented nicknames. 

There are many other such name collisions in every domain. Companies and products can share names, giving rise to trademarks to limit the usage of a given label within a domain. There are multiple YC companies called *Alpha* or *Level*. On the other hand, names can also be divergent. My previous employer, Vouch, showed up in some places as Vouch Inc., and Vouch Insurance in others. The company also used to be called SV InsureTech, but most often is just referred to as Vouch. 

Entity resolution (ER) is the process of identifying and linking multiple references to the same real-world entity across various data sources. In some businesses, de-duplicating and linking data correctly is existential. If you are a bank handing out loans, or an insurance company underwriting a new policy, you need to know who you are dealing with – not just for the sake of your margins but also to comply with regulatory mandates. It's not uncommon for a single entity to have multiple names, addresses, etc., which makes selling [Anti-Money Laundering](https://en.wikipedia.org/wiki/Anti%E2%80%93money_laundering) (AML) and [Know Your Customer](https://en.wikipedia.org/wiki/Know_your_customer) (KYC) software a big business. 

Leaning on my experience designing the data pipelines that created and maintained Vouch's knowledge graph of the startup ecosystem, in this blog post, I'll discuss some of the key ideas behind ER systems, and the challenges in building them.

**The Process**  
Imagine you are a home goods retailer reviewing product catalogs from suppliers. The items on offer have different names, wordy descriptions, some information about their manufacturers, and catalog-specific identifiers. In order to find the cheapest supplier for each item, say a dishwasher, you or your teammates could manually compare models across the catalogs. You'd work your way through them, maybe by matching manufacturer names first and looking at similarities between features later, comparing prices along the way. However, this process becomes impractical as the number of records and catalogs increase. If two catalogs contain 1000 dishwashers each, then there are 1 million pairs to examine, and that’s just operating on two relatively small sets of inputs. As more and larger catalogs are introduced, the task becomes too complex to be done manually. ER algorithms reduce the amount of work we need to do to establish canonical entities systematically and at scale.

Most ER systems follow a similar process.

1. Schema Alignment  
2. Cleaning/Standardization  
3. Blocking  
4. Matching/Linking  
   4a. Adding deterministic links  
5. Assigning virtual IDs  
6. Canonicalization/Summarization  
7. Evaluation

Let's break down each of these steps.

### 1. Schema Alignment
Like in most data problems, we start with messy data. Schema alignment is the process of mapping and standardizing data fields from different sources to a common set of attributes. For example, one of your appliance datasets might use `item_name` while another uses `model_name` - schema alignment would recognize these as equivalent and map them to a standardized field name. In some cases, a column might have to be split into multiple fields. For example, a person's name might be split into first, middle, and last names, or a manufacturer's name might be split into its legal name and its "doing business as" (DBA) name.  

<img src="https://cdn.faingezicht.com/er/er1.png" alt="Schema alignment">

The idea here is to end up with a single schema into which we can aggregate every record into, covering all sources, even if there might be some holes across datasets when there isn't a perfect column overlap. In the case where you have a single dataset with duplicates, which is referred to as a "clean" ER task, this step is not necessary.

### 2. Cleaning and standardization
Once we know which fields to compare, we need to ensure that they follow the same formats, or if they are numerical that they are in the same units of measurement. For example, the price column in one dataset might be in US Dollars while another is in Euros or, more subtly, one includes tax while another doesn't. Both of these cases require normalization. If working with dates, you want to parse them to all be in a single format (e.g., `YYYY-MM-DD`), or if working with URLs perhaps you want to cut them down to just the [fully qualified domain name](https://en.wikipedia.org/wiki/Fully_qualified_domain_name), removing subdomains and paths. Other strings might require removing punctuation, converting to lowercase, etc.  

#### Mappings

| Source    | Column Name        | Mapped Name             |
|-----------|--------------------|-------------------------|
| Catalog 1 | ID                 | source_id               |
| Catalog 1 | Manufacturer ID     | manufacturer_product_id |
| Catalog 1 | Manufacturer        | manufacturer_name       |
| Catalog 1 | Name               | product_name            |
| Catalog 1 | MSRP               | price_usd               |
| Catalog 2 | ID                 | source_id               |
| Catalog 2 | Brand              | manufacturer_name       |
| Catalog 2 | Product Name       | product_name            |
| Catalog 2 | Price (Euros)      | price_usd               |

Making sure data is comparable apples to apples helps with matching, in part because asserting equality is computationally much cheaper than fuzzy matching, but also because it ensures that the final dataset you generate is internally consistent.  


#### Consolidated Table

| Source   | source_id    | mfg_name          | product_name                          | mfg_product_id          | price_usd_cents |
|----------|--------------|-------------------|---------------------------------------|-------------------------|-----------------|
| Cat. 1   | 5678924      | Black & Decker    | Honeycomb™ Collection 2-Slice Toaster | TR1250WD1               | 5499            |
| Cat. 1   | 5674678      | Black and Decker  | 2-Slice Toaster                       | TR7827-1BD              | 1999            |
| Cat. 1   | 5678738      | Black & Decker    | 2-Slice Rapid Toaster                 | TR3501BS                | 4399            |
| Cat. 2   | a8adfd1378b6 | BLACKANDDECKER    | Honeycomb 2-Slice Toaster             |                         | 5250            |
| Cat. 2   | ca0b07325c8a | BLACKANDDECKER    | 2 Slice Toaster                       |                         | 1838            |
| Cat. 2   | 021b2c3bd759 | BLACKANDDECKER    | Two Slice Rapid Toaster               |                         | 3386            |


### 3. Blocking
As previously mentioned, one of the biggest problems with naive ER is the sheer number of comparisons that need to be made. This is what computer scientists would call an *N^2 problem*, where we'd compare every record to every other record. Blocking is how we reduce the search space by creating a smaller set of candidate pairs to compare. Specifically, the goal is to do a single pass on the dataset and assign each record a "blocking key" using only the information available on that record. In some cases, you might want to create a blocking key per attribute, like a company name or website, and in others, you might want to create a hybrid key that combines multiple attributes. Notice that you should not use the source of your data as a blocking key – nothing assures you that there aren't duplicate rows within a given input source.

On each box below, every row and column represents an entity, and every cell a comparison. On the leftmost we are doing every possible comparison. On the second, we have blocked the entities based on some rule into six distinct groups. Since we don't have to compare the entities to themselves, the third box removes those as well, and lastly since the comparisons are symmetric we only need to do them once per pair.

<img src="https://cdn.faingezicht.com/er/er4.png" alt="Blocking" style="width:100%;">
Blocking can be as simple as picking an existing categorical column to block on, or as complex as using a machine learning model to assign records to clusters. You probably block your socks when you're folding laundry, making separate piles by color and then matching corresponding pairs. Looking back to the retail catalog example, we could compare fridges to fridges and toasters to toasters, without comparing fridges to toasters. That works if every item is correctly labeled as one or the other, but sometimes we don't have such reliable categories. When working with businesses or people data we often have to get more creative. On the simpler side we could use the first letter of a name column for blocking. If we're concerned with typos, or variable spellings, we might pipe the data through a phonetic indexing algorithm like [Soundex](https://en.wikipedia.org/wiki/Soundex). If the attributes we are blocking on are numerical (like age or revenue) we can divide them into discrete bins and block records within the same bin. All of these are simple solutions, but on the other end of the spectrum complex clustering algorithms like [locality sensitive hashing](https://en.wikipedia.org/wiki/Locality-sensitive_hashing) or embeddings can help us bucket records, too. We might want to take into account multiple attributes to generate blocks, combining methods, but custom rules based on domain knowledge are often effective enough.

Each of the methods has trade-offs in computational complexity, accuracy, and explainability. The goal at this stage is to find a balance that works for your data while making the process faster by reducing the number of comparisons to be made.

While it might be tempting to use hybrid blocking and aggregate various fields into a single blocking key, the more complex the blocking keys you use the harder it is to understand and debug your system. I've found that the simpler comparison of one key at a time was a better approach, even if it required having multiple sets of blocking keys and more comparisons (one per attribute, plus a few smaller hybrid ones).

### 4. Matching and Linking
Once we have blocked the records, we iterate through the blocks and compare each pair of attributes or attribute groups within a block to decide if they are the same or not. Here, too, you can do something as simple as an equality check, which works for primary key-like values domain names or SSNs, or build a more complex model to account for typos, transcription errors, and other noise. Ultimately we are creating a binary classification model that takes a subset of the attributes of the record to predict if they are the same or not. Different measures can be used to process different attribute blocks, like using string a similarity metric like [Levenshtein distance](https://en.wikipedia.org/wiki/Levenshtein_distance) for names or [Jaccard similarity](https://en.wikipedia.org/wiki/Jaccard_index) to compare associated groups (say lists of friends on a social network, or a list of investments). You could even feed these to an LLM. Either way, you'll have to decide on a threshold for creating a link or not, which leads to similar trade-offs to those we saw when discussing blocking. Beyond simple rules, decision trees or logistic regression models are often good starting points.

This is an area where introducing domain knowledge is high leverage. For example, if you turned URLs into root domains before comparison, you might have two records whose links previously pointed to different apps on the App Store now both pointing to `apple.com`. The same problem comes up with GitHub links, social media accounts, etc. Creating hard coded rules to ignore these shared paths will improve the quality of your matches, but it also introduces new edge cases: the entity `Apple` can't be matched properly anymore, which could be a problem if you were trying to include all public companies in your dataset. On a similar vein, you should consider how to deal with subsidiaries, or related entities – should you match `amazon.com` with `amazon.co.uk`? Your business needs will guide you to different business logic.

### 4a. Adding deterministic links
In some cases, we can take advantage of already existing deterministic links between records. If your application code creates a record in an internal system like Salesforce or Zendesk, you can pass along the identifiers at creation-time to link records later in your ER system. If working with data about startups or SMBs you could have an offline process that follows DNS redirects offline, tracking that a URL like `usecompany.com` now redirects to `company.com`. These links are not based on the comparison of attributes, but on the knowledge you bake directly into the system.

Whether the links came from a probabilistic comparison system, or from a deterministic process, their downstream use is the same. The output of this step is a sequence of `(A, same_as, B)` triples, linking two records. In aggregate, all these links form a graph where each connected component represents N records. If our process works well we can assume, through transitivity, that each subcomponent represents a single real world entity. If you wanted to get fancy, you could assign each link a weight based on the confidence of the match, giving deterministic links a 100% confidence and get yet another threshold to tune on other links to decide if a link should be created or not.

### 5. Assigning virtual IDs
<img src="https://cdn.faingezicht.com/er/er5.png" alt="Virtual ID clusters" style="width:400px;">

At this point, we have a graph of linked records with many disconnected subgraphs. By performing a simple graph traversal, we can now assign a unique virtual identifier (VID) to each connected component. This could be a random UUID, but since a long lived system benefits from semi-stable identifiers we can do better. Hashing the attributes of the oldest record in the cluster is one such approach. If the cluster is split, the older half retains the original ID, while the newer half gets a new ID. This ensures that the ID remains stable even as the data changes.

One process that you can use to improve your data quality is to manually review the largest clusters produced by the ER system, as well as any totally unmatched entities. Tracking cluster size distribution, and the specific entities that land on either tail, will allow you to correct errors in the generated data by identifying overbearing or missing rules, as well as thresholds that are too strict or too lenient. This is a labor-intensive process, but it can be very effective in improving the quality of the data.

### 6. Canonicalization/Summarization
With our data connected, we have to decide which attributes to keep. If we have two records from different sources glued together with a `same_as` now we have two values for each of their fields. For example, source one might say that company `X` has 100 employees while source two says it has 110 employees. Which one do we keep? The process of choosing the right attributes is called canonicalization or summarization. The goal is to create a single record that represents the entity as accurately as possible. This is an area where ML can help with outliers, but domain knowledge and business rules can carry a lot of weight. This is a hard problem, which Nabeel Zewail and I discussed at length in [our talk at KGC'22, Modeling the Startup Ecosystem Using a Config Based Knowledge Graph](https://www.youtube.com/watch?v=MTZD5VTV4NI).

Adding to the complexity, we might have to deal with the temporal aspect of the data. The system we devised kept a date associated with each fact, which blew up both storage and computational costs but which allowed us to present the state of a summarized record "as of" a certain date. In general, we presented summaries as of the most recent date, but we could also present the state of the record at any point in time by running canonicalization on the fly on a filtered subset of associated records to an object. Generating a materialized view of the latest data then allowed us to serve the data quickly and efficiently, making it joinable with other datasets.

### 7. Evaluation
Finally, we need to evaluate the quality of our ER system, which we can do with a mix of online and offline metrics. Online metrics are those that help us measure the actual performance the model had in a real world setting, while offline metrics evaluate performance on historical data during model development and testing. Since there is no ground truth, online metrics are harder to compute so we end up using proxies like the number of input records, the number of output records, and the number of links created, as well as ratios between them. Keeping track across runs can tell us quickly if the system is working as expected: If we see that a run generated a ton of new clusters, several very large clusters, or many stand-alone clusters, we can assume something went wrong. Running our model on a static human-evaluated dataset allows us to check our results offline, and by comparing the output of the model to what a human would have guessed we can get a more nuanced view of where we're underperforming. However, curating these datasets is expensive, and it might not be obvious what needs fixing. Instead of trying to evaluate the entire system at once, it's better to evaluate each sub-model in the process separately. This way, you can identify where the system is failing and make targeted improvements. The evaluation process is iterative, and should be done regularly to ensure that the system is still working as expected.

This article is a brief survey, and each section could be a blog post of its own. To go deeper, I recommend the following articles, which helped me get a better understanding of the problems:

* [Practical Guide to Entity Resolution,](https://towardsdatascience.com/practical-guide-to-entity-resolution-part-1-f7893402ea7e) Yifei Huang, Palantir  
* [An overview of end-to-end entity resolution for big data,](https://blog.acolyer.org/2020/12/14/entity-resolution/) Adrian Colyer, Accel  
* [(Almost) All of Entity Resolution](https://unece.org/sites/default/files/2021-12/SDC2021_Day1_Steorts_P.pdf), Rebecca C. Steorts, Duke University  
* [The Five Generations of Entity Resolution on Web Data](https://raw.githubusercontent.com/AI-team-UoA/pyJedAI/main/docs/presentations/ICWE2024/5gER-Tutorial-Slides.pdf),  Konstantinos Nikoletos, Ekaterini Ioannou, George Papadakis, ICWE 2024 



<small>Thanks to Hannah Doherty and Ben Warren for reading drafts of this post.</small>
<hr>

<small>
<em>Photo: Metropolitan Stickers, by me. Previously posted on [New York City, 2018](/photos/2018/05/10/nyc2018/).
</em></small>
