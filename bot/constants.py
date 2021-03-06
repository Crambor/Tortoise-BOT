from enum import Enum

from discord import Color


tortoise_guild_id = 577192344529404154
website_url = "https://www.tortoisecommunity.ml/"
privacy_url = "https://www.tortoisecommunity.ml/pages/privacy"
rules_url = "https://www.tortoisecommunity.ml/pages/rules"
verification_url = "https://www.tortoisecommunity.ml/verification/"
github_repo_link = "https://github.com/Tortoise-Community/Tortoise-BOT"
tortoise_paste_service_link = "https://paste.tortoisecommunity.ml/"
line_img_url = "https://cdn.discordapp.com/attachments/581139962611892229/692712698487767080/animated_line.gif"


# Channel IDs
welcome_channel_id = 657704940080201739
announcements_channel_id = 578197131526144024
react_for_roles_channel_id = 603651772950773761

mod_mail_report_channel_id = 693790120712601610
bug_reports_channel_id = 693790120712601610
code_submissions_channel_id = 610079185569841153
suggestions_channel_id = 708734512296624239

# Log Channel IDs
system_log_channel_id = 593883395436838942
deterrence_log_channel_id = 597119801701433357
bot_log_channel_id = 693090079329091615
successful_verifications_channel_id = 581139962611892229
verification_channel_id = 602156675863937024
website_log_channel_id = 649868379372388352
bot_dev_channel_id = 692851221223964822
error_log_channel_id = 690650346665803777

# Roles
muted_role_id = 707007421066772530
verified_role_id = 599647985198039050
unverified_role_id = 605808609195982864

# Keys are IDs of reaction emojis
# Values are role IDs which will get added if that reaction gets added/removed
self_assignable_roles = {
    582547250635603988: 589128905290547217,     # python
    603276308084031511: 589129070609039454,     # java
    603647289902366723: 589129970820055080,     # go
    603276263414562836: 589129320480636986,     # javascript
    603274583772233728: 589808988506554398,     # rust
    603274784805224478: 591254311162347561,     # html
    603278259517390880: 589131517683433485,     # css
    603277646234779658: 589129183494406154,     # php
    603277725679222819: 589131126619111424,     # sql
    603277676714786914: 589131390944280577,     # ruby
    603275563972689942: 589131022520811523,     # c
    603275529587654665: 589129873809735700,     # c++
    603275597514407941: 589130125208190991,     # c#
    603277763293609990: 589129583375286415,     # r
    610825682070798359: 610834658267103262,     # events
    583614910215356416: 603157798225838101      # announcements
}


# Emoji IDs
mod_mail_emoji_id = 706195614857297970
event_emoji_id = 611403448750964746
bug_emoji_id = 690635117655359559
suggestions_emoji_id = 613185393776656384


# Captcha Verification
captchas = [("PRNU", "https://cdn.discordapp.com/attachments/581139962611892229/622697949914464286/"
                     "Example-of-PDM-character-extraction-for-the-animated-CAPTCHA-available-on-the-Sandbox.png"),
            ("PQJRYD", "https://cdn.discordapp.com/attachments/581139962611892229/622698143842172955/captche.jpg")]


# Music Options
# For all options see:
# https://github.com/ytdl-org/youtube-dl/blob/3e4cedf9e8cd3157df2457df7274d0c842421945/youtube_dl/YoutubeDL.py#L137-L312
ytdl_format_options = {
    "format": "bestaudio/best",
    "outtmpl": "downloads/%(extractor)s-%(id)s-%(title)s.%(ext)s",
    "restrictfilenames": True,
    "noplaylist": True,
    "nocheckcertificate": True,
    "ignoreerrors": False,
    "logtostderr": False,
    "quiet": True,
    "no_warnings": True,
    "default_search": "auto",
    "source_address": "0.0.0.0"  # ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
    'options': '-vn',
}

# Special
tortoise_developers = (197918569894379520, 612349409736392928)

# Embeds are not monospaced so we need to use spaces to make different lines "align"
# But discord doesn't like spaces and strips them down.
# Using a combination of zero width space + regular space solves stripping problem.
embed_space = "\u200b "

# After this is exceeded the link to tortoise paste service should be sent
max_message_length = 1000


class Infraction(Enum):
    warning = Color.gold()
    kick = Color.gold()
    ban = Color.red()


class SuggestionStatus(Enum):
    under_review = "Under review"
    denied = "Denied"
    approved = "Approved"
