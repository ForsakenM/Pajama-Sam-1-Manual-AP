# Welcome To My Pajama Sam 1 Manual AP World Randomizer!
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
4.  **Generate the Seed:** After saving your `Manual_PajamaSam1_ForsakenM.yaml` (and any other game YAMLs) to the `Players` folder, return to the Archipelago Launcher and click **Generate**. The client will generate your seed and, upon success, place an `AP_` zipped folder into your `output` folder.

### Phase 2: Hosting and Connecting.
1.  **Host the Server:** Head to the [Archipelago Host Page](https://archipelago.gg/uploads) and upload your zipped `AP_` folder. Once uploaded, click **Create New Room** to generate your 'SEED INFO' page, which displays your server's port number and the link to download your patch files.

> [!TIP]
>You can host your own server and room on your computer if you have the ability to do so by navigating to `Host` in your Archipelago Launcher (often at the top, easy to find!) and clicking Open, but it is most common to host via the Archipelago website.

2. **Connect to the Room:** * **Patch File:** Click **Download Patch File** on your room page. Opening this file will launch the **Manual Client**.
    * **Connect:** In the Manual Client, look at the **Server** textbox. Replace the default port (the 5 numbers after `archipelago.gg:`) with the specific 5-digit port found in your room's URL. Click **Connect**.
    * **Finalize:** Once connected, the client will ask for a **Slot Name**. Type or paste the exact name you used in your *Pajama Sam 1* YAML (also found on your room page) and press Enter.
    * **Ready:** Click the **Manual** tab in the client—you are now ready to play!

3.  **Play The Game!:** Fire up Pajama Sam 1 on your preferred device and enjoy a randomized adventure in the Land of Darkness!

## 🧩 Odds and Ends!

Have you lost all your stuff and don't know where to turn? While the combination of the Manual Client and the Universal Tracker should sort out your lost socks, if you still find yourself stuck in the Land of Darkness you can check out my [Google Doc](https://docs.google.com/document/d/186y1VHYymWI91IeoipwO6wKrhLrZ4L3X9vjmES9zVuc/edit?usp=sharing) that will have a deeper dive into the items, locations, traps, and overall logic of the manual!

If you are still having issues, feel free to reach out to the Manual For Archipelago Discord Server! If it's an issue with the Manual Client or of a similar nature, they can help you out! If you are still confused on the logic or if their might be an AP World issue, feel free to ping me in the `Pajama Sam 1` channel!

The above Google Doc will also list planned updates, and I encourage those who enjoy the manual to feel free to discuss ideas for it in the Discord channel, as well as for anyone with manual experience to give me any advice. Most AP projects are a labor of love, and I'm just getting started and have a lot to learn, so please feel free to coach me! :)

And above all, thank you for checking out and playing my manual! :D