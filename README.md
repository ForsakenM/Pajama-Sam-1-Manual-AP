# Welcome To My Pajam Sam 1 Manual AP World Randomizer!
Hello and welcome to my Pajama Sam in No Need To Hide When It's Dark Outside, most often referred to as Pajama Sam 1!

Pajama Sam 1 is a point-and-click adventure game made by Humongous Entertainment with the intent of it being interactive educational content for children, but there is a certain amount of nostolgia tied to the educational games of that era and I wanted to breathe new life into the genre via Archipelago!

This is my first manual I've created and really my first major attempt or contribution to anything Archipelago related, and I'm excited to start my journey here, so I hope you enjoy playing my manual!

## 🎒 What You'll Need To Play!

To get started, ensure you have the following components installed:

* **[Archipelago Launcher](https://github.com/ArchipelagoMW/Archipelago/releases)**: The core software required to host and join Multiworlds.
* **[Manual Client](https://github.com/ManualForArchipelago/Manual/releases)**: The specialized client that allows you to track your items and locations.
* **[Pajama Sam 1 .apworld](https://github.com/ForsakenM/Pajama-Sam-1-Manual-AP/releases)**: My custom manual file (available in the **Releases** section of this repo).
* A copy of the game! ([Steam](https://store.steampowered.com/app/283960/Pajama_Sam_No_Need_to_Hide_When_Its_Dark_Outside/), [GOG](https://www.gog.com/en/game/pajama_sam_vol_1), [Nintendo Switch](https://www.nintendo.com/us/store/products/pajama-sam-no-need-to-hide-when-its-dark-outside-switch/), [PS4](https://store.playstation.com/en-us/product/UP2035-CUSA35530_00-3616316769034939), [IOS/App Store](https://apps.apple.com/us/app/pajama-sam-no-need-to-hide/id582442437), [Android/Google Play](https://play.google.com/store/apps/details?id=com.tommo.nggpepj1&hl=en_US)).


> [!TIP]
> While not required to play, having the latest version of the [Universal Tracker](https://github.com/FarisTheAncient/Archipelago/releases?q=Tracker) is not only incredibly helpful in general for knowing what locations are considered in logic as you are playing in any Archipelago session or reporting logic issues to apworld creators, but it is especially helpful with the Manual Client as it causes all locations that are in logic to be highlighted!

## 🛠️ Getting Everything Ready!
### Phase 1: Setup and Generation.

1.  **Install the APWorlds:** Copy your downloaded `.apworld` files for the Pajama Sam 1 manual, the Manual Client, and the Universal Tracker and paste them into your `/Archipelago/custom_worlds` folder. 
> [!TIP]
> If the Archipelago Launcher was already open, close and restart it so it can "see" your new manual files. Otherwise, the next step in the process can fail as the Archipelago Launcher may not reconize the addition of new `.apworld` files.

2.  **Generate your .yaml:** Open your Archipelago Launcher and navigate to `Generate Template Options` and click Open. This will open a window to your `Templates` folder that lists all the yaml files for all your apworlds you have installed while also generating new yaml files for apworlds you just recently installed.

3.  **Customize and Save:** In your `Templates` folder, find a yaml file named `Manual_PajamaSam1_ForsakenM.yaml` and open it. Customize it based on the experience you want while playing, then save the edited yaml file in your `/Archipelago/Players` folder.

> [!TIP]
> For more information and guidance on how to customize/edit yaml files for intended gameplay experience, reach out to the Archipelago or Manual for Archipelago Discord servers, or check out the [Archipelago Website](https://archipelago.gg/) for further assistance/instruction.

4.  **Generate the Seed:** Once you have saved your edited `Manual_PajamaSam1_ForsakenM.yaml` and the yamls of any other games you wish to play in your `Players` folder, return to your Archipelago Launcher and navigate to `Generate` and click Open. The Archipelago client will then work on generating the seed for all your included yamls. If it generates successfully, you will find a zipped folder with a name that begins with 'AP_' and then a string of numbers following the underscore in your `output` folder within your `Archipelago` folder.

### Phase 2: Hosting and Connecting.
7.  **Host the Server:** Now we need to get a server ready and hosting! Head to the [Host Game page on the Archipelago Website](https://archipelago.gg/uploads) and upload your zipped folder that is in your `output` folder. Give it some time depending on how many yamls were involved in generation as well as possible high traffic on the website, then it will load a page with 'SEED INFO'. Click 'Create New Room' and it will load a page with the created room that displays information such as the port number for your room's server, each player's name, the game they are playing, and a link to any patch files needed to download.

> [!TIP]
>You can host your own server and room on your computer if you have the ability to do so by navigating to `Host` in your Archipelago Launcher (often at the top, easy to find!) and clicking Open, but it is most common to host via the Archipelago website.
>It's best practice to click the 'Download' link on the 'SEED INFO' page so that you have access to your Spoiler Log in case all participating players get stuck and are unsure of how to progress. You can either navigate this file yourself (WARNING: this will spoil you on the intended solution to the multiworld!) or you may be able to provide it to someone in the corresponding game's Archipelago/Manual for Archipelago's Discord channel for some hints without spoiling yourself entirely. Using Universal Tracker or a Poptracker for your respective game tends to help avoid needing to do this, but it never hurts to do just in case!

8.  To start playing your Pajama Sam 1 Manual from here, you will click the 'Download Patch File' link in your room on the Archipelago website, then once the patch file is downloaded open it. It should automatically open the Manual Client (though it might take a little bit). Once the Manual Client opens, you will take the port number from your room on the Archipelago website (the five numbers at the end of '/connect archipelago.gg:') and paste them over the five numbers at the end of 'archipelago.gg:' in the Server textbox in the Manual Client, then click the 'Connect' button. Once the Manual Client connects with the server, it will ask for a slotname which is your name from your Pajama Sam 1 yaml, which is also on the room webpage. Type or copy/paste your name in the Command textbox and enter it to finalize connection to the server and you can click the Manual tab in the client and it should be ready to go!

9.  Fire up Pajama Sam 1 on your preferred device and enjoy the manual!