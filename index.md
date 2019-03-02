# Privacy Plan

Hello! This website aims to give you **a list of concise, actionable steps** that you can take to improve your privacy online. You don't have to do all of them, but the more you do, the better.

It also has some security tips, but note that **sometimes security is antithetical to privacy**. I tried to keep everything to a good balance, but you might need to make some decisions yourself. Decisions you can make are marked and explained as such.

> Disclaimer: Anything you do with this guide is your own responsibility. The information on this website is provided as-is and is contributed by volunteers.

You're welcome to ask for help, clarifications, etc. - but please remember that responses are not guaranteed.

## Helpful Features of this Website

Each step may have **substeps or options** that are sometimes marked as EASY, MODERATE, or DIFFICULT for the slightly-above-average user. You can use these tags to comb through low hanging fruit before needing to make big changes.

## Step: Switch your Internet Browser

You have a couple options here. 

- EASY: Use [Firefox](https://www.mozilla.org/en-US/firefox/new/)! Just download it and be sure to install the recommended browser extensions (and as little other extensions as possible).
- MODERATE: Use [Firefox](https://www.mozilla.org/en-US/firefox/new/), and customize it! You can do this by installing an [FFProfile](https://ffprofile.com).
- If you **must** use Chrome... try [ungoogled-chromium](https://github.com/Eloston/ungoogled-chromium). (SECURITY: Technically the official Chrome browser is better for security than ungoogled-chromium, since Google is a registered company that would probably not distribute viruses. The author of ungoogled-chromium, assuming good faith on their part, could get hacked much more easily. This is a tradeoff you will have to decide on your own. If you decide against using ungoogled-chromium, you will unfortunately need to stay with Chrome.)

## Step: Fix Your Browser Addons

Keep in mind that **you should not get addons other than these**. If you have to get an addon, check if it's open source (how to do this is an exercise for the reader). **An addon not being open source is a red flag!** It doesn't neccesarily mean that it's bad, but it most likely does.

That said, get these addons!

- EASY: UBlock Origin | [Firefox](https://addons.mozilla.org/addon/ublock-origin/) | [Chrome](https://chrome.google.com/webstore/detail/ublock-origin/cjpalhdlnbpafiamejdnhcphjbkeiagm) | [Edge](https://www.microsoft.com/store/p/app/9nblggh444l4) | [Safari](https://github.com/el1t/uBlock-Safari#ublock-originfor-safari) - This is the best adblocker you can use. **Note that it is NOT UBlock (which comes up on the first page of Google search).** Use the links I provided to install it for your respective browser to ensure that you don't get the wrong one.
  - Why use an adblocker? Ads are the reason you get tracked. If you want to support content creators, try donating to their patreon/liberapay or similar.

That's basically all you *need*, the rest are just small extras.

- MODERATE: Multi-Account Containers | [Firefox](https://addons.mozilla.org/en-US/firefox/addon/multi-account-containers/) - Use one container for each service that tracks you. You might not be able to eliminate the service entirely, but at the very least you can limit them.
  - Other ideas: Use one container for work, one container for personal/general browsing, and one for social media.

**UNINSTALL THE FOLLOWING:**

- Ghostery - It's owned by an ad company. Need I say more?
- Any Coupon Extension - They're also mostly owned by ad companies, and track your browser history.
- AdBlock - Use UBlock Origin instead, see above.
- Grammarly - It sends everything you type to them, and has been vulnerable in the past. Do not use.

## Step: Stop Using Services That Track You

**If you're not using "end to end encrypted" services, they can see all the data you send to them.** Just "encrypted" is not enough, be sure to look for the "end to end encrypted" or "E2E" wording, or the service might be using your information.

This specific step is fully covered by other excellent websites, so in the spirit of collaboration, I will just link to them here:

- [Prism Break](https://prism-break.org/en/) - A list of alternatives to services that track you. Click on what type of computer/phone you have and see what you can replace.
- [PrivacyTools.io](https://www.privacytools.io) - "knowledge and tools to protect your privacy against global mass surveillance"
- [Switching.social](https://switching.social) - Specifically good for switching social networking websites, but they list other alternatives as well.
- [Framasoft](https://degooglisons-internet.org) - A company that makes open source software. They list their own software and also competitor's software, as long as it's still free.

Note that some of these will be hard to do, but others should be relatively easy (like notes apps, or calendar apps, since you can usually move your data out of those and into the replacement.)

## Step: Use a Password Manager

Okay, this one isn't really a privacy tip. It's a security tip. There are three options for you here.

- EASY: [BitWarden](https://bitwarden.com) - You should use an Open Source password manager.
- EASY: [1Password](https://1password.com) - This is if you have no idea what you're doing and kind of just want everything to work, but you still want to be secure.
- HARD: [Selfhost Bitwarden](https://help.bitwarden.com/article/install-on-premise/) - You can store your own data yourself too. Highly not recommended unless you have experience with Linux and hosting servers.

## Step: Delete (or Replace) Social Media

I get it. **For a lot of people, this will be indescribably hard.** Other than using an adblocker, this might be the single most effective thing to do on this list. **You want to keep up with your friends and family**, and you probably feel like Facebook is the only way that you can do this.

That said, here's an interesting thought experiment. **If your friends aren't your friends anymore because you deleted Facebook, were they ever really your friends?** I *know* it makes it harder to talk to them. I *know* it's super painful. But most of all, I know that it still needs to be done.

**Everyone is different, but here's how it worked out for me.** I deleted all my proprietary social media. My close friend group uses a group chat, so I still have plenty of social interactions on my phone. I can send iMessages to everyone with iPhones, and I can talk to everyone else over the phone or in person. I still talk to people online through open social media. I'm pretty happy about it and I don't really feel like I'm missing out on much (although I definitely thought I was at first).

If you feel the need to talk about yourself and maintain social media, that's fine too. Just be sure to use these platforms instead of Twitter / Facebook / Instagram / Snapchat / etc.

- [Mastodon](https://joinmastodon.org/) - A microblogging site (think twitter, tumblr). The website I linked explains everything else. This is the most popular and easiest to use "truly free" social media.
- There are more that you can find at [switching.social](https://switching.social), but note that not all of them explain everything as well as Mastodon does. If you're new to federated social networks I'd highly recommend watching and reading about Mastodon *first*, as it has the best-explained resources in general.

## Step: Switch your Email Service

Your email address is the entry point to your digital life. Everything you sign up for, do, or say, is linked to your email address. **It is the ultimate tracking identifier, and most of us are giving up all of the information in it to companies like Google and Microsoft.**

**Switching your email service is pretty hard.** Every service you signed up for will need to be slowly moved over, but it doesn't need to be done all at once. Just sign up for new services with your new email, and slowly move old ones over as time permits.

That said, it's not all bad news. When you move off GMail, you can get custom email addresses! Mine is just "hi @ myname.com" - but you could make it ANYTHING (for $8 a year). **Imagine how cool you can be!** :smile:

Here are some services that I can recommend:

- [Tutanota](https://tutanota.com/) - You can't connect an email client to this! If you only check your email online, this is fine, but know that you won't be able to use Outlook, Thunderbird, Apple Mail, etc. It's relatively cheap at 12 EUR / year, and there is a limited free tier.
- [Protonmail](https://protonmail.com) - Although you can connect an email client to this, it's somewhat difficult and buggy right now. I wouldn't count on it working, but the option is there for Mac, Windows, or Linux. It's slightly more expensive at 48 EUR / year, but there is a limited free tier.
- [FastMail](https://fastmail.com/) - I use this, but as it's based in [Australia](https://www.youtube.com/watch?v=eW-OMR-iWOE) and not end-end encrypted, I'm not so sure anymore. Maybe hold off on signing up...
- And of course, check out the "replacement" websites under the "Stop Using Websites That Track You" section. Some of them have good lists of email providers.

## Step: Change Your Phone

Here it is, in order from worst to best (in terms of privacy).

- Google Android - This is what you buy from Samsung, LG, etc. It has Google apps and tracking built in! Don't use this!
- iOS - It does have some tracking, but a lot of the really invasive things are encrypted, so it's a little bit better.
- Open Android - You can't buy this, but it's what you will get if you install a privacy-focused custom ROM (and don't install Google Apps) onto a phone.
- Pure Linux - Phones like the Librem 5 or Ubuntu Touch exist, but know that you're *probably* (they aren't readily available) going to have a considerably worse experience on these than anything else. They might be okay if you live in an area that supports them, and you only need a web browser/calling/texting/other basics.

Basically, use iOS if you don't know how to install custom ROMs, and use custom ROMs if you do.

## This isn't the end!

Security and privacy start with you! Be conscious of what you're sharing online with the world, and be vigilant for red flags when browsing day to day. Hopefully this guide helped you, but it won't protect you from anything and everything.

---

Made by [Nikhil Jha](https://nikhiljha.com/) and [Others](https://github.com/nikhiljha/privacyplan). This work is licensed under a [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/). You can contribute on the [Git Repository](https://github.com/nikhiljha/privacyplan).