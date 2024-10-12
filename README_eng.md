## Server Registration Bot (PERFECT FOR ROLEPLAY SERVERS)

This bot provides a user registration system for Discord servers. Members can be interviewed by the registration team when they join the server, and necessary information is collected and recorded. Additionally, various logs are kept regarding the registration process, and the number of registrations handled by the staff is tracked.

## Languages and Libraries Used

<picture>
  <source srcset="https://skillicons.dev/icons?i=py" media="(prefers-color-scheme: dark)">
  <img src="https://skillicons.dev/icons?i=py,sqlite">
</picture>
discord.py, pytz, datetime, asyncio, logging

### Features

1. **Assign Unregistered Role:** When new members join the server, they are automatically assigned the `unregistered` role.
2. **Welcome Message:** A welcome message is sent privately to the new member, explaining how to register on the server.
3. **Registration Form:** To register a member, a form is created, asking for the following information:
   - Roblox Username
   - IC (In Character) Name
   - Roblox Profile Link
   - Character Backstory
4. **Registration System:** Once the registration process is completed, the user's registration is logged, and they are officially registered on the server.
5. **Staff Registration Count:** A command allows staff to view how many people they have registered.
6. **Database:** Registration numbers are stored in an SQLite database and can be queried as needed.

### Requirements

- Python 3.8+
- Discord.py 2.0 or higher
- `pytz`, `sqlite3`, `logging`, `asyncio` libraries

### Installation Steps

1. **Install Python and Required Libraries:**
   ```bash
   pip install discord.py pytz
   ```

2. **Running the Bot:**
   - Create a bot on the Discord Developer Portal and grant the necessary permissions.
   - Paste your bot token in the line: `bot.run("your discord token paste here")`.
   - Run the bot in the terminal with the following command:
     ```bash
     python bot.py
     ```

3. **Database Setup:**
   The SQLite database will be created automatically when the bot runs, along with the necessary tables.

### Commands

1. **/register**
   - Description: Registers a user to the server.
   - Usage: `/register @user roblox_username ic_name roblox_link character_backstory`
   - Permissions: Only users with specified `registrar` roles can use this command.

2. **/registercount**
   - Description: Displays the registration count for staff.
   - Usage: `/registercount`
   - Permissions: Only those who can use the registration command can view this.

### Logging

- Registration processes and bot activities are logged using Python's `logging` module. Errors and important events are displayed in the console.

### Customization

- **IDs:** Replace server-specific `role`, `channel`, and `staff` IDs with your server's IDs.
- **Bot Prefix:** The default command prefix is set to `.`. You can change it in the line `commands.Bot(command_prefix='.')`.

### Troubleshooting

- **Bot Not Working:** Double-check your Discord token and ensure the proper permissions are granted.
- **Role/Permission Errors:** Make sure the bot has the required permissions and that the correct role IDs are set.

### Developer Info

This bot is designed to speed up the registration process within the server and keep track of registration logs. It uses the new application commands introduced in Discord.py 2.0 and above to enhance its functionality.

---

If you encounter any issues, feel free to contact me: githubsupport@l1ve709.com / Instagram: l1ve709


## My Discord Account
![My Discord](https://lantern.rest/api/v1/users/794909914760871967?svg=1&theme=dark&borderRadius=2&hideActivity=1&hideStatus=0)
