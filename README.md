# Nakamori -- A Kodi addon for Shoko

---------------------------------------------------------

As some of you may have discovered, Kodi does not handle anime well. With lots of edits to the naming conventions and elaborate folder structures and separate metadata files, you can get a very nice result, but how long does that take every time you get a new series? [Shoko](https://shokoanime.com) solves this problem by recognizing files by their data, not by a name or location. Unfortunately, Shoko Desktop was made for just that: Desktop computers. Kodi has a nice 10 foot interface, and Shoko has a lot of data to show. Nakamori brings them together.

## Features

- Watched States, Resuming, and Scrobbling
  Nakamori syncs your watched states, progress, and votes automatically to Shoko. No extra work needs to be done. It has convenient context menu items to mark entire series and groups, as well. Since it is synced to Shoko, you can grab a laptop or tablet and finish watching on-the-go.
- Group Filters
  Nakamori has full support for displaying Shoko Group Filters, from Continue Watching to directory style filters like Years, Tags, and Seasons. You can create all kinds of filters in Shoko Desktop and choose to hide or show them in Nakamori.
- Grouping
  A less known feature of Shoko is the ability to automatically group seasons and related anime together. No more fiddling with [Bakemonogatari](http://anidb.net/perl-bin/animedb.pl?show=rel&aid=6327). We've been there, and we took care of it. Nakamori supports these without any extra effort.
- Fuzzy Searching
  Can you spell Hououin Kyouma without googling it? Well, the rest of us appreciate a search that doesn't insist you commit seppuku when you butcher an innocent foreign name. It's common, so don't worry if you're one of them. There is an entertaining ongoing bug that makes results not show when you spell it exactly right, but it's not on purpose. We swear.
- Lots of Display Options
  Aside from supporting basically every skin in existence, we take the approach of more settings is better than less. I might know what looks good better than you, but why should you care! If you want to make the text red and illegible, that's your choice! Don't want spoilers? Hide them! I don't care, but *you* might.
- More! Probably...
  I may be a developer who spends *way* too much time making a program to sort my Chinese Cartoon Porn™, but I forget things, too. Maybe I got lazy and didn't feel the need to update this document. Maybe I spent weeks rewriting everything because I think it's ugly and then didn't care enough to tell anyone. This is in active development by several people, so in the worst case, just shoot us a message. We're around.

## Thanks

This was initially based on [JAVStream](http://www.ptom.co.uk/home/). The code is far from it at this point, but they still deserve a thanks.
[plugin.video.plexbmc](https://github.com/hippojay/plugin.video.plexbmc/) showed how to do some stuff for UI and other handy things.
A big thanks to the Kodi community for helping with many Kodi related issues over the years.
An even bigger thanks to the Kodi Team for never giving up, no matter how annoying we all are.

## FAQ

**Q: I can't connect or something?**
**A:** This **NEEDS** Shoko Server to do anything. The default connection details are 127.0.0.1:8111 (the computer it's running on at port 8111). The default userpass creds are: `Default` with a blank password. Make sure the IP is pointing to the computer that Shoko Server is running on, and that no firewalls or other *fun* is getting in the way.

**Q: My watched states are acting...weird.**
**A:** That's not a question, but it is weird. This can happen when you use Kodi's built-in Mark as Watched function (pressing W or the button at the bottom of the context menu). There's a button in the Addon Settings, under Browsing at the very bottom, to fix these. If that doesn't help, contact us. It might be a bug.

**Q: Why are the images for things mixed up?**
**A:** There are a few reasons it could happen. Below the button mentioned right above this, there's a button to clear Kodi's image cache. If that doesn't help, then open Shoko Desktop and see if the TvDB link matches the show. Sometimes the automatic search is wrong. At the least, it's usually funny.

**Q: I keep getting an error about file offset?**
**A:** This can happen for a few reasons. The most common is that you have a poor connection to the server. The second most common is that your client can't keep up trying to play the file due to crap hardware and/or old software. I have the issue on occasion with my 8-core dev machine with 10GbE to the disk array. Kodi is old and they need more help. If it's a constant issue and/or you just want it gone, then you can disable the resume feature in Addon Settings -> Video.

**Q: What should I do if an error window pops up that wasn't on the list?**
**A:** If it's just once, and it stops, ignore it. If it keeps happening, tell us. There's an Issue list above, or hop on [discord](https://discordapp.com/invite/vpeHDsg) and ask in the #nakamori or #support channel.

**Q: Something...happened...I don't know?**
**A:** Yeah, shit happens. Shoko is old. We try, but there are bugs. The first thing we'll tell you is to check if it shows the proper response in Desktop. If it does, then it's probably an issue in the API or Nakamori. Tell us about it, and we can go from there.

**Q: Why are you such an ass?**
**A:** I'm a programmer. I literally make things just to watch them break unintentionally. I'm considerate enough to explain it, and I have plenty of patience if you're willing to give me your time and be reasonable. Just remember that every one of us does this for free because we want to. Don't be that guy who thinks that we need to be nice. We are nice because no one gives a reason not to be. We are all smart enough to teach computers how to recognize and sort anime in multiple languages, too, so if we feel that you need to be made a fool of, we are capable. That said, we are all nice people most days, so try not to let the blunt sarcasm scare you away if you just need help or want to chill.
