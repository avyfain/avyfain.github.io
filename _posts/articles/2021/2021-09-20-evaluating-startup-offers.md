---
title: How to Evaluate Startup Offers - A Beginner's Guide
layout: post
tags: [startups, jobs, tech, san francisco]
main_image: vaxd-travel/previews/2.jpeg
category: articles
description: If you're joining a startup for money, you're doing it for the wrong reasons, but that doesn't mean that money shouldn't factor into your decision. You can build financial models around salaries and equity, and I'll show you how to do that below.
---


<small>TL;DR, [here](https://docs.google.com/spreadsheets/d/1AW0WVzsaEQOan_oHHIFHO0lAfpjtATsywe18hvh1H3Q/edit?usp=sharing) is a sample spreadsheet you can duplicate to evaluate your offers.</small>

<small><em>Este ensayo también está disponible [en español](/articles/2021/09/20/evaluating-startup-offers-es/).</em></small>


I recently [decided to leave my big tech job](https://faingezicht.com/2021/04/16/heres-to-the-crazy-ones/) at Apple, where I had been for 6 years, to join a startup called [Vouch](vouch.us/) (we're [hiring](vouch.us/careers)!). As I was considering the switch, multiple people told me I was making a big mistake, losing out on both job stability and compensation. Those people had no idea what they were talking about. If you're joining a startup for money, you're doing it for the wrong reasons, but that doesn't mean that money shouldn't factor into your decision.

You can build financial models around salaries and equity, and I'll show you how to do that below, but remember your job experience will give you _[intangibles](https://www.investopedia.com/terms/i/intangibleasset.asp)_ that you can't represent in a spreadsheet. A FAANG offer will win on sheer numbers every time. If you have flexibility, pick your next job based on how it can help you get to where you want to end up. Only you can tell whether you value the stability of a brand name or learning how to navigate a bureaucracy more or less than seeing a new business come to life or experiencing hypergrowth. The people you'll work with and the network you'll build matter a lot, too. Make sure you have a clear north star, or you'll have a much harder time making a choice. For example, when I [chose to join Vouch](https://faingezicht.com/articles/2021/04/26/new-beginnings/), I tried to maximize my learning about the venture ecosystem and how startups operate.

If you are considering taking a role at a startup, the framework below should give you basic tools to compare startup offers, but it doesn't pretend to give you exact answers.


### 1. How venture capital funding works

When you hear that a startup has raised a round with an eye-popping valuation, all that means is that there was a venture capital (VC) firm willing to buy a portion of their business for cash, and the startup was willing to take their deal. The figures they agree to imply the company's new valuation. Startups use other financial instruments to raise capital, but the standard venture fundraise is simply that: an inflow of dollars matched by the issue of new shares of **preferred stock**, creating value almost out of thin air.

To illustrate the mechanics, let's imagine[^1] a company raising a seed round from a single firm:

* Before the deal, the startup has 10M shares outstanding.
* A VC firm values the company at $5M _pre-money_ and agrees to invest $1M on that price. This effectively gives the company a _post-money_ valuation of $6M.
* The valuation implies a price for the company's outstanding shares. Since _pre-money_ the 10M shares are worth $5M, the price is $5M / 10M shares = $0.50/share
* In exchange for the $1M, the company will issue new shares and hand them to the VC. The number of shares issued is mostly a matter of accounting: ($1M) / ($0.50/share) = 2M new shares. Now the company has 10M + 2M = 12M shares outstanding.
* At this point, an additional set of **common shares** could be issued to create/restock the [employee option pool](https://carta.com/blog/how-to-size-employee-option-pool/). These shares would also factor into pricing but we'll ignore them to keep the analysis simple.

For shareholders, the fundraise is usually good news. However, they now own a smaller piece of a larger pie. When your percentage of ownership is decreased via the issuance of new shares you're experiencing **dilution**. If you were the lucky holder of 100,000 shares, you used to own 1% of the company. After this round, you only own 0.83%, and future rounds of funding will further dilute your shares.

There are many nuances to startup funding[^2], but the basics described above on how equity is priced and how those prices evolve throughout a company's life are a big part of the puzzle. [Most startups fail](https://www.failory.com/blog/startup-failure-rate), but if you're lucky, you'll join one of the few that is not worth $0 in the long run.


### 2. Compensation package structure and options

On top of your salary and maybe a signing bonus, startups offer equity as part of their compensation. Employee ownership is ingrained in the startup mentality for a reason. Stock compensation aligns incentives, translating employees' hard work to potential shared gains. At the same time, it allows companies to offer the prospect of a big payout in the future in exchange for a smaller paycheck today.

While bigger companies might offer stock in the form of RSUs, which are functionally similar to the public company shares you could buy on a brokerage account, smaller startups give their employees [stock options](https://www.investopedia.com/terms/o/option.asp) instead. These securities come in many different flavors, mostly differing on tax rules, but to keep things simple we'll assume we're talking about [incentive stock options (ISOs)](https://carta.com/blog/what-are-incentive-stock-options/). An ISO gives the holder the right to buy a share of common stock in the future, at a prespecified price. This is called the **strike price**, and it comes from an independent appraisal of the fair market value (FMV) of the stock. It is interchangeably called the **409a valuation**, after the [section](https://en.wikipedia.org/wiki/Internal_Revenue_Code_section_409A) in the IRS code that regulates it. The strike price you're offered will always be a fraction of the most recent preferred share price, set so that the current value of common stock makes your options nominally worth $0, ensuring no tax events are triggered when the employee receives them.

Using the example from before, the $0.50 preferred stock price paid by the investors might translate to a strike price of $0.15[^3]. At this price, when a prospective employee is offered $50k in equity she'd get a grant for 100,000 options. If the company does poorly, those options might end up being [underwater](https://www.investopedia.com/terms/u/underwater.asp) and worthless, but let's assume the company does well, and that a few years down the line their shares are priced at $50 (a 100x increase!). This lucky employee has the right to **exercise** her options, redeeming shares by paying $15,000 ($0.15 * 100,000 options) to get $5M worth of stock ($50 * 100,000 shares).

But we're getting ahead of ourselves. Even before the equity gets to appreciate, it needs to **vest**. Big equity numbers sound exciting to a hypothetical new-joiner, but getting a grant upon signing her offer doesn't mean that equity will immediately be transferred to her. Once again this is about incentive alignment. If she immediately got her equity, she could quit the next day. To ensure people are committed for the long run, the industry-standard vesting schedule spreads the distribution over four years, with a one year **cliff**. During the first year of employment, the employee doesn't get any equity. After hitting the cliff at the one year mark, the first 25% of the grant vests, and every month after that another 2.0833% (75% over 36 months) hits her account.

The terms discussed above vary a bit from company to company, and some might be cagier than others about giving up this information during negotiation. Two valuable terms to ask about are [early exercise](https://www.cooleygo.com/early-exercisable-stock-options-what-you-need-to-know/) and exercise windows[^4]. In essence, at the time you leave the company, you'll have a limited amount of time to shell out cash to turn your vested options into shares. The standard window used to be [90 days after leaving](https://zachholman.com/posts/fuck-your-90-day-exercise-window/), although some companies have started to change to favor employees with multi-year windows. These terms will have a big impact on net compensation.

Transparency in valuation and prices is a signal of a well-run operation, an open culture, and a healthy business. If they don't share those numbers it might mean things aren't going that well. A dollar number on an equity package means nothing without the broader context. You should always ask for specific numbers for:

* Total shares outstanding
* Last preferred price
* 409a/strike price
* Number of options in your grant

Armed with these values, and setting aside a lot of complexity about taxation, we can move on to the calculations that will allow us to compare various offers.

### 3. Expected value
If you have taken a basic probability class, feel free to skip this section.

Expected value is what it sounds like: a way to measure the potential outcome of something that has an unknown value today — such as the valuation of a startup in 5, 10, or 20 years.

Let’s use a coin flip as an example. If it comes up heads, you get $100. If it comes up tails, you get $0. The expected value (denoted as E[x]) is defined as the sum of the outcomes weighted by the probability that each one might occur:

    E[x] = (½ * $0) + (½ * $100) = $50

True, under this payout scheme no one bet over a coin flip will ever reward you with $50, but the anticipated value is still clearly given by this weighted sum. If you repeat the coin flip a thousand times on average you'd end up at $50, as [the law of large numbers](https://en.wikipedia.org/wiki/Law_of_large_numbers) tells us. More complex events can be modeled similarly. If you toss a standard 6-sided die, the expected value to be rolled is 3.5, even if no roll can ever have its outcome suspended between 3 and 4:

    (⅙ * 1) + (⅙ * 2) + (⅙ * 3) + (⅙ * 4) + (⅙ * 5) + (⅙ * 6) = 3.5

Applying this idea, you can estimate the future value of anything: the expected rewards from pulling the arm on a slot machine, the return on buying a new house, the price of Apple stock tomorrow, or the potential payoff of your startup IPOing. The nuance here is that unlike a coin flip where the odds are well understood and discrete (half the time you'll see heads, and half the time tails) and the payoffs are well defined ($0 or $100) most interesting problems involve more uncertainty. With a slot machine, the player doesn't really know the payoff structure, nor the probability distribution, even though they're both baked into the game by its designer. In the housing, stock, and venture markets, not only are the payoffs and their probability distributions unknown to us, but they are not defined by anyone else. They are emergent phenomena.

Uncertainty about uncertainty is the reason why there's a whole industry devoted to analyzing patterns in the noise. Just like there is expected value, there's also a way to measure [expected risk](https://www.investopedia.com/terms/r/risk.asp), which I'll leave for a different blog post.


### 4. Discounted cash flow analysis

If you have taken a basic finance class, feel free to skip this section.

Evaluating any financial project requires accounting for [the time value of money](https://www.investopedia.com/terms/t/timevalueofmoney.asp). On top of the uncertainty aspects discussed earlier, the payment schedule for most startups is asymmetrical: You’re accepting less compensation today for the promise of a potential payout later. Setting aside any liquidity constraints (e.g. wanting to save $X/year for a down payment, or needing $Y/month to pay your student loans and rent), we need some way to account for that time difference to calculate the real value of any offer on the table.

In short, the problem we're solving is that $1 today is worth more than $1 tomorrow. With $1 today, you can pay off $1 of debt, and avoid accruing interest on it; or you can put it in the bank and earn that interest yourself. The process of laying out projects side by side to compare their returns is called [discounted cash flow](https://www.investopedia.com/terms/d/dcf.asp) analysis, or DCF.

For example, assuming there's a bank willing to pay you a rate of r = 1% on your cash, you know that depositing $100 today means having $101 next year. The math also works the other way around, though, and we can see that if

    ($100 today) * (1 + 1%) = $101 next year

then

    $100 today =  ($101 next year) / (1 + 1%)

Abstractly,

    $X today = $X next year/(1+r)

Dividing by that factor is called discounting. You can use the same logic to discount further into the future, dividing each cash flow by (1+r) again each period.

    $X next year/(1+r) = ($X in two years/(1+r))/(1+r) = $X in two years/(1+r)^2

The further out you go the more the discounting will eat away at the value of those future cash flows. Picking [the right value for r](https://twitter.com/avyfain/status/1372198641910288386) is a science of its own, but in some ways it represents the alternative uses you'd have for that cash if you had it today.

For example, let's imagine two startups. One offers you a higher starting salary and steady pay increases, while the other lets you know they won't give you a raise after your first year, promising bigger payouts down the line.


<table>
  <tr>
   <td>
   </td>
   <td>Year 1
   </td>
   <td>Year 2
   </td>
   <td>Year 3
   </td>
   <td>Year 4
   </td>
  </tr>
  <tr>
   <td>Offer A
   </td>
   <td><p style="text-align: right">
$110</p>

   </td>
   <td><p style="text-align: right">
$115</p>

   </td>
   <td><p style="text-align: right">
$120</p>

   </td>
   <td><p style="text-align: right">
$125</p>

   </td>
  </tr>
  <tr>
   <td>Offer B
   </td>
   <td><p style="text-align: right">
$100</p>

   </td>
   <td><p style="text-align: right">
$100</p>

   </td>
   <td><p style="text-align: right">
$120</p>

   </td>
   <td><p style="text-align: right">
$150</p>

   </td>
  </tr>
</table>


If we choose r = 5%, for example, we can discount those cash flows to get to each offers' [net present value](https://www.investopedia.com/terms/n/npv.asp) (NPV):

    NPV(A) = $110 + $115/(1+r) + $120/(1+r)^2 + $125/(1+r)^3 = $415.57
    NPV(B) = $100 + $100/(1+r) + $120/(1+r)^2 + $150/(1+r)^3 = $413.01

If we naively add up each stream of payments they both add up to $470, but the pay structure is very different and (merely financially) you'd be better off taking A's offer than B's. The NPV you end up with depends entirely on the value you pick for r.


### Evaluating your offer

Now let's put it all together, getting into [scenario](https://www.investopedia.com/terms/s/scenario_analysis.asp) and [sensitivity](https://www.investopedia.com/terms/s/sensitivityanalysis.asp) analysis.

Let's go back to hypothetical companies, but now instead of just assuming sure exits, let's model out these payments based on expected values, including dilution and exercise costs. This is where scenario analysis comes in. You can guesstimate the odds of potential outcomes based on what you know about the market - just make sure to always err on the side of being too negative, not too optimistic.

You can find a spreadsheet you can copy and edit to plug in your own values [here](https://docs.google.com/spreadsheets/d/1AW0WVzsaEQOan_oHHIFHO0lAfpjtATsywe18hvh1H3Q/edit?usp=sharing).

![Equity Spreadsheet]({{ site.image_path }}evaluating_startup_offers/equity_tool.png
 "Equity Spreadsheet")

The values in the light blue represent offer terms that will be given to you by the person you're negotiating with (this is why transparent terms matter). The values in red can be filled-in based on what you learned in the interviews, and your own research about the market. How big can this startup really get? Lastly, the values in yellow are rough rules of thumb around dilution which will depend on what round the company is currently on, and overall market sentiment.

You can build a table like this one to model scenarios for the offers you have at hand. For simplicity, the sheet linked above makes assumptions across offers that don't need to hold. For example, all these fictional startups exit after 4 years, but you could model uncertainty around that as well. Take the sheet as a template and update it to fit your needs. You could further extend the calculations to include dilution from additional funding rounds, secondary sales, [refresh/evergreen grants](https://review.firstround.com/The-Right-Way-to-Grant-Equity-to-Your-Employees), etc. Ultimately, what we're looking for is to boil down each offer to a set of future expected cash flows, which we can then discount at different rates.

In the sample linked above, for example, Foo Inc gives a very nice salary and bonus up front but meager exit potential, while Bar.ly and Baz.io's compensation weighs a lot more on the potential exit. On paper, it looks like Bar.ly isn't offering very compelling compensation.

![NPV Sensitivity Analysis]({{ site.image_path }}evaluating_startup_offers/NPV_sensitivity_analysis.png
 "NPV Sensitivity Analysis")

Only your gut can tell you which one feels right from here on. VCs get to make many small bets with their fund. That gives them a lot more leeway to be wrong on multiple counts while still turning a profit. When picking your new job you are putting all your eggs in one basket, so you better pick one where the bottom is unlikely to drop out. This is why choosing a startup just for the financial possibilities is a bad idea. If you have a couple of options that check the boxes on what you're looking for, and you're equally excited about them, only then it comes down to the financials. If the equity is worth $0, will you have learned the things that you want to learn? Will you meet the right people? Will you work closely enough with the leadership team? These won't show up in any financial model, but probably matter a lot more in the long arc of your career.

### A few thoughts on negotiating

Most startups are willing to trade equity for cash. If you need to pay off student loans, or are otherwise cash-strapped, you can ask for more cash and less equity. If you can live on a smaller paycheck, and truly believe in the vision, you can ask for more equity and take on that risk. If you feel like you have leverage, asking for two offers, one with high equity and low salary and vice versa, can give you a hint at how they value their own stock. Asking for more equity is often easier than more cash, depending on their funding and option pool situation, but having both offers can give you an idea of what an all-cash offer would look like for this startup, which is a valuable data point in itself.

I'll leave the rest of my negotiating advice for a different post, but if you're looking for help on that front I'd recommend you read [Patrick McKenzie's guide](https://www.kalzumeus.com/2012/01/23/salary-negotiation/).

Do you have your own modeling suggestions, negotiation tips, startup advice, general feedback, or any questions? [I'd love to hear it](/contact/page/).

<small>_This is the third in a series I’m writing about my recent career transition out of Apple. See part one, on [things I learned in my time at Apple](https://faingezicht.com/2021/04/16/heres-to-the-crazy-ones/), and part two, on [how I picked my role at Vouch](https://faingezicht.com/articles/2021/04/26/new-beginnings/). Make sure to check back in a few weeks for upcoming pieces on **things to ask in interviews with startups**, and **tips on how to make your job transition as smooth as possible**, etc._<small>

Thanks to Hannah Doherty, Max Faingezicht, Moi Stern, and Sandeep Paruchuri for their feedback on drafts of this post.

<hr>
<small><em>Photo: Big Wheel, Las Vegas, by me. Previously posted on [Vax'd Travel](/photos/2021/07/10/vaxd-travel/).</em></small>
<hr>


[^1]:
    Lifted from Y Combinator's [fundraising guide](https://www.ycombinator.com/library/4A-a-guide-to-seed-fundraising)

[^2]:
     If you want to scratch the surface, [Brad Feld's Venture Deals](https://bookshop.org/books/venture-deals-be-smarter-than-your-lawyer-and-venture-capitalist/9781119594826) is the book to get started.

[^3]:
     This implies a FMV of 30% of the latest round's valuation. While the appraisal is a much more complex process, depending on the round, ⅕ to ⅓ of the preferred price is a standard rule of thumb to follow.

[^4]:
     Both of these are out of scope for this blog post, but the former can have a big impact on your taxes, while the latter might make your options worth even less than you thought if your financial situation doesn't allow you to acquire your stock.
