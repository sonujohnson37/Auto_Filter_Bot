class script(object):
    START_TXT = """<b><u>Hello,Dude i'am Anya</u></b>

<b>Oii!{}, {}</b>

<b>🐼Hey<a href=https://t.me/{}>{}</a>, My Owner is everything to me.</b>
"""


    GSTART_TXT = """<b> Hello Dude's I'm Anya </b>

<b>Oii!{},</b>

<b>🕊️Hey!<a href=https://t.me/{}>{}</a>, I will only give Anime series .</b>"""

    
    HELP_TXT = """<b>
    
✨How to request anime✨  
🔍 Search the correct spelling on google.  
💬 Send the name in the group .  
🧾 Use this format:  

🗡️ For Anime:  
➤ Anime name + S01 (For season 1, Change for others) 
</b>"""

    ABOUT_TXT = """<b>╭────[My Details ]────⍟
├My Name: <a href=https://t.me/{}>{}</a>
├Developer: <a href={}>ᴏᴡɴᴇʀ</a> 
├Library : <a href='https://docs.pyrogram.org/'>ᴘʏʀᴏɢʀᴀᴍ</a>
├Language : <a href='https://www.python.org/download/releases/3.0/'>ᴘʏᴛʜᴏɴ 𝟹</a> 
├Database : <a href='https://www.mongodb.com/'>ᴍᴏɴɢᴏ ᴅʙ</a> 
├Bot Server : <a href='https://heroku.com/'>ʜᴇʀᴏᴋᴜ</a> 
├Build Status : ᴠ1.4 [ ꜱᴛᴀʙʟᴇ ]
╰───────────────⍟</b>"""
    RESTART_TXT = """
<b>{} Bot Restarted!
🗓️ Date : <code>{}</code>
⏳ Time : <code>{}</code>
🌐 Timezone : <code>Asia/Kolkata</code>
🛠️ Build Status: <code> v1.4 [ Sᴛᴀʙʟᴇ ]</code>
</b>"""

    CHANNELS = """
<b>⚡ ɢʀᴏᴜᴘs & ᴄʜᴀɴɴᴇʟs ɪɴғᴏ ⚡ 

▫ All New Anime series.
▫ Fastest Bots are added.
▫ Free and easy to use.
▫ 24x7 Service Available.</b>"""

    MULTI_STATUS_TXT = """<b>╭────[ 🗃 ᴅᴀᴛᴀʙᴀsᴇ 1 🗃] ────⍟</b>
│
├⋟ All Users ⋟ <code>{}</code>
├⋟ All Groups ⋟ <code>{}</code>
├⋟ Premium Users ⋟ <code>{}</code>
├⋟ All Files ⋟ <code>{}</code>
├⋟ Used Storage ⋟ <code>{}</code>
├⋟ Free Storage ⋟ <code>{}</code>
│
<b>├────[ 🗳 Database 2 🗳 ]────⍟</b>   
│
├⋟ All Files ⋟ <code>{}</code>
├⋟ Size ⋟ <code>{}</code>
├⋟ Free ⋟ <code>{}</code>
│
<b>├────[👾Bot Details👾 ]────⍟</b>   
│
├⋟ Uptime ⋟ {}
├⋟ Ram ⋟ <code>{}%</code>
├⋟ Cpu ⋟ <code>{}%</code>   
│
├⋟ Both DB Files: <code>{}</code>
│
<b>╰─────────────────────⍟</b>"""

    STATUS_TXT = """<b>╭────[ 🗃 ᴅᴀᴛᴀʙᴀsᴇ 🗃 ]────⍟</b>
│
├⋟ All User's ⋟ <code>{}</code>
├⋟ All Groups ⋟ <code>{}</code>
├⋟ Premium Users ⋟ <code>{}</code>
├⋟ All Files ⋟ <code>{}</code>
├⋟ Used Storage ⋟ <code>{}</code>
├⋟ Free Storage ⋟ <code>{}</code>
│
<b>├────[👾Bot Details👾]────⍟</b>   
│
├⋟ Uptime ⋟ {}
├⋟ Ram ⋟ <code>{}%</code>
├⋟ Cpu ⋟ <code>{}%</code>   
│
<b>╰─────────────────────⍟</b>"""

    LOG_TEXT_G = """#NewGroup
    
Group = {}
ID = <code>{}</code>
Total Members = <code>{}</code>
Added By - {}
"""

    LOG_TEXT_P = """#NewUser
    
ID - <code>{}</code>
Name - {}
"""
    NT_ADMIN_ALRT_TXT = """✨ You are not admin in this group """

    NT_ALRT_TXT = """Not Your's!"""
    
    ALRT_TXT = """Oii {},
This is not your anime request,
Request Yourself..."""

    OLD_ALRT_TXT = """Oii {},
You are using one of my old message , 
Please Send the request again."""

    PRE_STREAM = """🔒 This Feature is only for 🏅 Premium User's 

✨ Unlock Exclusive Content and Features  
💳 Buy premium to get started """

    PRE_STREAM_ALERT = """⚠️ Premium Content 
🔓 Unlock it by upgrade to premium """

    CUDNT_FND = SPELLING_ERROR_TXT = """<b> Spelling Mistake Dude!</b>  
<b>😊 No Worries —Check Spelling Down There 👇</b>

<blockquote>👇Spelling Mistake Dude</blockquote>"""


    DEL_MSG = """⚠️ This Anime File Deleted in <b><u><code>{}</code></u></b>

<blockquote expandable><b><i>Please Forward this file somewhere else & Download it From there</i></b></blockquote>"""





    I_CUDNT = """<b>Sorry, Are you really searching for anime file {} 😶

Check your spelling in Google and try again 😃

🧾 Series Request Format 📜

 Example : Death Note S01 or Death Note S01E04

🧸 Don't Use':(!,./)</b>"""
    
    I_CUD_NT = """<b>I couldn't find any anime related to {}.

Anime not available reason  :

1) ᴏ.ᴛ.ᴛ or DVD not released

2) Type Name with year 

3) Anime is not available in the database report to admin </b>"""

    MVE_NT_FND = NOT_FOUND_TXT = """<b>😌 This Anime is not Available in my database.</b>

<blockquote>😌 Anime not found </blockquote>"""

    
    TOP_ALRT_MSG = """Searching for query in my database..."""

    MELCOW_ENG = """<b>👋 Oii {},\n\n🍁 Welcome to\n🌟 {} \n\n🔍 Here you can search for your favourite anime by typing its name 🔎\n\n⚠️ If you're having trouble downloading or something else then message here👇</b>"""
    
    DISCLAIMER_TXT = """
<b>This is an open source project .

ᴀʟʟ ᴛʜᴇ ꜰɪʟᴇꜱ ɪɴ ᴛʜɪꜱ ʙᴏᴛ ᴀʀᴇ ꜰʀᴇᴇʟʏ ᴀᴠᴀɪʟᴀʙʟᴇ ᴏɴ ᴛʜᴇ ɪɴᴛᴇʀɴᴇᴛ ᴏʀ ᴘᴏꜱᴛᴇᴅ ʙʏ ꜱᴏᴍᴇʙᴏᴅʏ ᴇʟꜱᴇ. ᴊᴜꜱᴛ ꜰᴏʀ ᴇᴀꜱʏ ꜱᴇᴀʀᴄʜɪɴɢ ᴛʜɪꜱ ʙᴏᴛ ɪꜱ ɪɴᴅᴇxɪɴɢ ꜰɪʟᴇꜱ ᴡʜɪᴄʜ ᴀʀᴇ ᴀʟʀᴇᴀᴅʏ ᴜᴘʟᴏᴀᴅᴇᴅ ᴏɴ ᴛᴇʟᴇɢʀᴀᴍ. ᴡᴇ ʀᴇꜱᴘᴇᴄᴛ ᴀʟʟ ᴛʜᴇ ᴄᴏᴘʏʀɪɢʜᴛ ʟᴀᴡꜱ ᴀɴᴅ ᴡᴏʀᴋꜱ ɪɴ ᴄᴏᴍᴘʟɪᴀɴᴄᴇ ᴡɪᴛʜ ᴅᴍᴄᴀ ᴀɴᴅ ᴇᴜᴄᴅ. ɪꜰ ᴀɴʏᴛʜɪɴɢ ɪꜱ ᴀɢᴀɪɴꜱᴛ ʟᴀᴡ ᴘʟᴇᴀꜱᴇ ᴄᴏɴᴛᴀᴄᴛ ᴍᴇ ꜱᴏ ᴛʜᴀᴛ ɪᴛ ᴄᴀɴ ʙᴇ ʀᴇᴍᴏᴠᴇᴅ ᴀꜱᴀᴘ. ɪᴛ ɪꜱ ꜰᴏʀʙɪʙʙᴇɴ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ, ꜱᴛʀᴇᴀᴍ, ʀᴇᴘʀᴏᴅᴜᴄᴇ, ꜱʜᴀʀᴇ ᴏʀ ᴄᴏɴꜱᴜᴍᴇ ᴄᴏɴᴛᴇɴᴛ ᴡɪᴛʜᴏᴜᴛ ᴇxᴘʟɪᴄɪᴛ ᴘᴇʀᴍɪꜱꜱɪᴏɴ ꜰʀᴏᴍ ᴛʜᴇ ᴄᴏɴᴛᴇɴᴛ ᴄʀᴇᴀᴛᴏʀ ᴏʀ ʟᴇɢᴀʟ ᴄᴏᴘʏʀɪɢʜᴛ ʜᴏʟᴅᴇʀ. ɪꜰ ʏᴏᴜ ʙᴇʟɪᴇᴠᴇ ᴛʜɪꜱ ʙᴏᴛ ɪꜱ ᴠɪᴏʟᴀᴛɪɴɢ ʏᴏᴜʀ ɪɴᴛᴇʟʟᴇᴄᴛᴜᴀʟ ᴘʀᴏᴘᴇʀᴛʏ, ᴄᴏɴᴛᴀᴄᴛ ᴛʜᴇ ʀᴇꜱᴘᴇᴄᴛɪᴠᴇ ᴄʜᴀɴɴᴇʟꜱ ꜰᴏʀ ʀᴇᴍᴏᴠᴀʟ. ᴛʜᴇ ʙᴏᴛ ᴅᴏᴇꜱ ɴᴏᴛ ᴏᴡɴ ᴀɴʏ ᴏꜰ ᴛʜᴇꜱᴇ ᴄᴏɴᴛᴇɴᴛꜱ, ɪᴛ ᴏɴʟʏ ɪɴᴅᴇx ᴛʜᴇ ꜰɪʟᴇꜱ ꜰʀᴏᴍ ᴛᴇʟᴇɢʀᴀᴍ. 
</b>"""

    DREAMXBOTZ_DONATION = DONATE_TXT = """<b>👋 ʜᴇʏ {},</b>

<blockquote>💖 <b>ᴘʟᴇᴀꜱᴇ ᴅᴏɴᴀᴛᴇ ᴛᴏ ᴛʜᴇ ᴅᴇᴠᴇʟᴏᴘᴇʀ</b></blockquote>

<b>🔧 ᴛᴏ ᴋᴇᴇᴘ ᴛʜɪꜱ ꜱᴇʀᴠɪᴄᴇ ᴀʟɪᴠᴇ, ᴀᴅᴅ ɴᴇᴡ ꜰᴇᴀᴛᴜʀᴇꜱ & ᴜᴘʟᴏᴀᴅ ʙᴇꜱᴛ ᴍᴏᴠɪᴇꜱ/ᴡᴇʙꜱᴇʀɪᴇꜱ ɴᴏɴ-ꜱᴛᴏᴘ ɪɴ ʜɪɢʜ Qᴜᴀʟɪᴛʏ, ᴡᴇ ɴᴇᴇᴅ ʏᴏᴜʀ ꜱᴜᴘᴘᴏʀᴛ.
ɪᴛ ʜᴇʟᴘꜱ ᴜꜱ ᴘᴀʏ ꜰᴏʀ ʜᴇʀᴏᴋᴜ & ꜱᴇʀᴠᴇʀ ʀᴇꜱᴏᴜʀᴄᴇꜱ.</b>

<b>🌝 ʏᴏᴜ ᴄᴀɴ ᴅᴏɴᴀᴛᴇ ᴀɴʏ ᴀᴍᴏᴜɴᴛ ʏᴏᴜ ʜᴀᴠᴇ.</b>

<blockquote>🎉 <b>ꜱᴇʟᴇᴄᴛ ʏᴏᴜʀ ᴅᴏɴᴀᴛɪᴏɴ ᴍᴇᴛʜᴏᴅ 👇</b></blockquote>

➤ 📷 Qʀ ᴄᴏᴅᴇ → <a href='{}'>ᴄʟɪᴄᴋ ʜᴇʀᴇ ᴛᴏ ꜱᴄᴀɴ</a>  
➤ 💸 ᴜᴘɪ ɪᴅ → <code>{}</code>

‼️ <b>ᴍᴜꜱᴛ ꜱᴇɴᴅ ꜱᴄʀᴇᴇɴꜱʜᴏᴛ ᴀꜰᴛᴇʀ ᴅᴏɴᴀᴛɪɴɢ.</b>"""


    SINFO = """
⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯
ꜱᴇʀɪᴇꜱ ʀᴇǫᴜᴇꜱᴛ ꜰᴏʀᴍᴀᴛ
⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯

ɢᴏ ᴛᴏ ɢᴏᴏɢʟᴇ ➠ ᴛʏᴘᴇ ꜱᴇʀɪᴇꜱ ɴᴀᴍᴇ ➠ ᴄᴏᴘʏ ᴄᴏʀʀᴇᴄᴛ ɴᴀᴍᴇ ➠ ᴘᴀꜱᴛᴇ ᴛʜɪꜱ ɢʀᴏᴜᴘ

ᴇxᴀᴍᴘʟᴇ : Death Note S01E01

🚯 ᴅᴏɴᴛ ᴜꜱᴇ ➠ ':(!,./)"""

    NORSLTS = """ 
#NoResults

Iᴅ : <code>{}</code>
Nᴀᴍᴇ : {}

Mᴇꜱꜱᴀɢᴇ : <b>{}</b>"""
    
    CAPTION = """<b><a href="https://t.me/iqmoviesa">{file_name}</a></b>\n\n<b>🧡 Powered By: <a href="https://t.me/iqmoviesa">[IQAnime🧡]</a></b>"""

    
    MOVIE_UPDATE_NOTIFY_TXT = """
</b><a href={poster_url}>📥</a><a href={imdb_url}>New {tag} Added</a></b>

<blockquote>✨ Title : <code>{filename}</code>


📹 Genres : <b>{genres}</b>
📺 OTT       : <b>{ott}</b>
🎞️ Quality: <b>{quality}</b>
🎧 Audio    : <b>{language}</b>
☄️ Rating   : <b>{rating}</b>
{episodes}
</blockquote>


🔍 <b>Search →</b> {search_link}
"""


    IMDB_TEMPLATE_TXT = """<b><a href={url}>{title} (<a href={url}/releaseinfo>{year}</a>)

ʀᴀᴛɪɴɢ : <a href={url}/ratings>{rating}</a>
ɢᴇɴʀᴇ : {genres}
ᴀᴜᴅɪᴏ : {languages}

sʜᴏᴡɴ ɪɴ : {remaining_seconds} <i>sᴇᴄ</i>⚡️
<b>ʀᴇǫ ʙʏ : {message.from_user.mention}</b>"""

    LOGO = r"""
    ██████╗░██████╗░███████╗░█████╗░███╗░░░███╗██╗░░██╗██████╗░░█████╗░████████╗███████╗
    ██╔══██╗██╔══██╗██╔════╝██╔══██╗████╗░████║╚██╗██╔╝██╔══██╗██╔══██╗╚══██╔══╝╚════██║
    ██║░░██║██████╔╝█████╗░░███████║██╔████╔██║░╚███╔╝░██████╦╝██║░░██║░░░██║░░░░░███╔═╝
    ██║░░██║██╔══██╗██╔══╝░░██╔══██║██║╚██╔╝██║░██╔██╗░██╔══██╗██║░░██║░░░██║░░░██╔══╝░░
    ██████╔╝██║░░██║███████╗██║░░██║██║░╚═╝░██║██╔╝╚██╗██████╦╝╚█████╔╝░░░██║░░░███████╗
    ╚═════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═════╝░░╚════╝░░░░╚═╝░░░╚══════╝

    𝙱𝙾𝚃 𝚆𝙾𝚁𝙺𝙸𝙽𝙶 𝙿𝚁𝙾𝙿𝙴𝚁𝙻𝚈....
    """


    #PLANS

    PAGE_TXT = """Why are you so curious  ⁉️"""

    PURCHASE_TXT = """Select your payment method ."""

    

    PREMIUM_TEXT = """<blockquote>🎖️ <b>Available Plans</b></blockquote>


◉ 07 ᴅᴀʏꜱ - 10 ₹  / 10 ꜱᴛᴀʀ
◉ 15 ᴅᴀʏꜱ - 20 ₹  / 20 ꜱᴛᴀʀ
◉ 30 ᴅᴀʏꜱ - 40 ₹  / 40 ꜱᴛᴀʀ
◉ 45 ᴅᴀʏꜱ - 55 ₹  / 55 ꜱᴛᴀʀ
◉ 60 ᴅᴀʏꜱ - 75 ₹  / 75 ꜱᴛᴀʀ

•─────•─────────•─────•
🏷️ <a href='https://t.me/iqmoviesa'>ꜱᴜʙꜱᴄʀɪᴘᴛɪᴏɴ ᴘʀᴏᴏꜰ</a>

‼️ ᴍᴜꜱᴛ ꜱᴇɴᴅ ꜱᴄʀᴇᴇɴꜱʜᴏᴛ ᴀꜰᴛᴇʀ ᴘᴀʏᴍᴇɴᴛ.
‼️ ᴀꜰᴛᴇʀ ꜱᴇɴᴅɪɴɢ ꜱᴄʀᴇᴇɴꜱʜᴏᴛ ɢɪᴠᴇ ᴜꜱ ꜱᴏᴍᴇᴛɪᴍᴇꜱ ᴛᴏ ᴀᴅᴅ ʏᴏᴜ ɪɴ ᴘʀᴇᴍɪᴜᴍ ʟɪꜱᴛ."""

    PREMIUM_STAR_TEXT = """<b><blockquote>ᴘᴀʏᴍᴇɴᴛ ᴍᴇᴛʜᴏᴅ: ᴛᴇʟᴇɢʀᴀᴍ ꜱᴛᴀʀꜱ ⭐</blockquote>

ɴᴏᴡ ʏᴏᴜ ᴄᴀɴ ʙᴜʏ ᴏᴜʀ ᴘʀᴇᴍɪᴜᴍ ꜱᴇʀᴠɪᴄᴇ ᴜꜱɪɴɢ ᴛᴇʟᴇɢʀᴀᴍ ꜱᴛᴀʀꜱ.  

ɪꜰ ʏᴏᴜ ꜰᴀᴄᴇ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ, ᴛᴀᴋᴇ ᴀ ꜱᴄʀᴇᴇɴꜱʜᴏᴛ ᴀɴᴅ ꜱᴇɴᴅ ɪᴛ ᴛᴏ - @deendayal_Support_group

ꜱᴇʟᴇᴄᴛ ʏᴏᴜʀ ᴅᴇꜱɪʀᴇᴅ ᴀᴍᴏᴜɴᴛ ᴀɴᴅ ᴘᴜʀᴄʜᴀꜱᴇ ᴀ ꜱᴜʙꜱᴄʀɪᴘᴛɪᴏɴ 👇.</b>
"""

    PREMIUM_UPI_TEXT = """<b><blockquote>ᴘᴀʏᴍᴇɴᴛ ᴍᴇᴛʜᴏᴅ: ᴜᴘɪ</blockquote>

ʏᴏᴜ ᴄᴀɴ ᴘᴜʀᴄʜᴀꜱᴇ ᴘʀᴇᴍɪᴜᴍ ᴛʜʀᴏᴜɢʜ ᴜᴘɪ , ɴᴇᴛ ʙᴀɴᴋɪɴɢ.

💳 ᴜᴘɪ ɪᴅ - <code>{}</code>

💢 ᴍᴜꜱᴛ ꜱᴇɴᴅ ꜱᴄʀᴇᴇɴꜱʜᴏᴛ ᴀꜰᴛᴇʀ ᴘᴀʏᴍᴇɴᴛ.

‼️ ᴀꜰᴛᴇʀ ꜱᴇɴᴅɪɴɢ ꜱᴄʀᴇᴇɴꜱʜᴏᴛ ᴘʟᴇᴀꜱᴇ ɢɪᴠᴇ ᴜꜱ ꜱᴏᴍᴇᴛɪᴍᴇ ᴛᴏ ᴀᴅᴅ ʏᴏᴜ ɪɴ ᴘʀᴇᴍɪᴜᴍ ʟɪꜱᴛ.</b>"""


    PREMIUM_END_TEXT = """<b>ʜᴇʏ {},</b>

<b>ʏᴏᴜʀ ᴘʀᴇᴍɪᴜᴍ ᴀᴄᴄᴇss ʜᴀs ʙᴇᴇɴ ʀᴇᴍᴏᴠᴇᴅ.</b>  
<b>ᴛʜᴀɴᴋ ʏᴏᴜ ꜰᴏʀ ᴜsɪɴɢ ᴏᴜʀ sᴇʀᴠɪᴄᴇ 😊</b>  
<b>ᴄʟɪᴄᴋ ᴏɴ /plan ᴛᴏ ᴄʜᴇᴄᴋ ᴏᴜʀ ᴏᴛʜᴇʀ ᴘʟᴀɴs.</b>

  BPREMIUM_TXT = """<blockquote>🎁<b>ᴘʀᴇᴍɪᴜᴍ ꜰᴇᴀᴛᴜʀᴇꜱ</b> :</blockquote>

○ ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴠᴇʀɪꜰʏ
○ ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴏᴘᴇɴ ʟɪɴᴋꜱ
○ ᴅɪʀᴇᴄᴛ ꜰɪʟᴇꜱ   
○ ᴀᴅ-ꜰʀᴇᴇ ᴇxᴘᴇʀɪᴇɴᴄᴇ 
○ ʜɪɢʜ-ꜱᴘᴇᴇᴅ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ                         
○ ᴍᴜʟᴛɪ-ᴘʟᴀʏᴇʀ ꜱᴛʀᴇᴀᴍɪɴɢ ʟɪɴᴋꜱ                           
○ ᴜɴʟɪᴍɪᴛᴇᴅ ᴍᴏᴠɪᴇꜱ & ꜱᴇʀɪᴇꜱ                                                                        
○ ꜰᴜʟʟ ᴀᴅᴍɪɴ ꜱᴜᴘᴘᴏʀᴛ                              
○ ʀᴇǫᴜᴇꜱᴛ ᴡɪʟʟ ʙᴇ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ɪɴ 1ʜ [ ɪꜰ ᴀᴠᴀɪʟᴀʙʟᴇ ]

• ʏᴏᴜ ᴄᴀɴ ɢᴇᴛ ᴘʀᴇᴍɪᴜᴍ ʙʏ ʀᴇꜰᴇʀɪɴɢ ʏᴏᴜʀ ꜰʀɪᴇɴᴅꜱ ᴏʀ ʏᴏᴜ ᴄᴀɴ ʙᴜʏ ᴘʀᴇᴍɪᴜᴍ ꜱᴇʀᴠɪᴄᴇ 

•─────•─────────•─────•
◉ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ : /myplan

‼️ ᴀꜰᴛᴇʀ ꜱᴇɴᴅɪɴɢ ꜱᴄʀᴇᴇɴꜱʜᴏᴛ ɢɪᴠᴇ ᴜꜱ ꜱᴏᴍᴇᴛɪᴍᴇꜱ ᴛᴏ ᴀᴅᴅ ʏᴏᴜ ɪɴ ᴘʀᴇᴍɪᴜᴍ ʟɪꜱᴛ."""  


    PREPLANS_TXT = PREMIUM_TXT = """<b>👋 ʜᴇʏ {},

<blockquote>🎖️ <b>ᴀᴠᴀɪʟᴀʙʟᴇ ᴘʟᴀɴꜱ</b></blockquote>

◉ 07 ᴅᴀʏꜱ - 10 ₹  
◉ 15 ᴅᴀʏꜱ - 20 ₹  
◉ 30 ᴅᴀʏꜱ - 40 ₹  
◉ 45 ᴅᴀʏꜱ - 55 ₹  
◉ 60 ᴅᴀʏꜱ - 75 ₹  

•─────•─────────•─────•

🏷️ <b>ᴘᴀʏᴍᴇɴᴛ ᴍᴇᴛʜᴏᴅꜱ</b>

💸 ᴜᴘɪ ɪᴅ → <code>{}</code>  
📷 ǫʀ ᴄᴏᴅᴇ → <a href='{}'>ᴄʟɪᴄᴋ ʜᴇʀᴇ ᴛᴏ ꜱᴄᴀɴ</a>  

🧾 ᴘᴀʏ ᴀᴄᴄᴏʀᴅɪɴɢ ᴛᴏ ʏᴏᴜʀ ᴘʟᴀɴ ᴀɴᴅ ᴇɴᴊᴏʏ ᴘʀᴇᴍɪᴜᴍ!

‼️ ᴍᴜꜱᴛ ꜱᴇɴᴅ ꜱᴄʀᴇᴇɴꜱʜᴏᴛ ᴀꜰᴛᴇʀ ᴘᴀʏᴍᴇɴᴛ.  
‼️ ᴀꜰᴛᴇʀ ꜱᴇɴᴅɪɴɢ ᴀ ꜱᴄʀᴇᴇɴꜱʜᴏᴛ, ɢɪᴠᴇ ᴜꜱ ꜱᴏᴍᴇ ᴛɪᴍᴇ ᴛᴏ ᴀᴅᴅ ʏᴏᴜ ɪɴ ᴛʜᴇ ᴘʀᴇᴍɪᴜᴍ ʟɪꜱᴛ.

💎 ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴘʟᴀɴ → /myplan</b>"""


    FREE_TXT = """<b>👋 ʜᴇʏ {},
    
🎉 <u>ꜰʀᴇᴇ ᴛʀɪᴀʟ</u> 🎉
❗ ᴏɴʟʏ ꜰᴏʀ 5 ᴍɪɴᴜᴛᴇꜱ
 
○ ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴏᴘᴇɴ ʟɪɴᴋꜱ
○ ᴍᴜʟᴛɪ-ᴘʟᴀʏᴇʀ sᴛʀᴇᴀᴍɪɴɢ ʟɪɴᴋs
○ ᴀᴅ-ғʀᴇᴇ ᴇxᴘᴇʀɪᴇɴᴄᴇ

👨‍💻 ᴄᴏɴᴛᴀᴄᴛ ᴛʜᴇ <a href='https://t.me/iqmoviesa'>Owner</a> ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ᴛʀɪᴀʟ.

➛ ᴜꜱᴇ /plan ᴛᴏ ꜱᴇᴇ ᴀʟʟ ᴏᴜʀ ᴘʟᴀɴꜱ ᴀᴛ ᴏɴᴄᴇ.
➛ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ ʙʏ ᴜꜱɪɴɢ : /myplan</b>"""

    
    UPI_TXT = """<b>👋 ʜᴇʏ {},
    
 ᴘᴀʏ ᴀᴍᴍᴏᴜɴᴛ ᴀᴄᴄᴏʀᴅɪɴɢ ᴛᴏ ʏᴏᴜʀ ᴘʟᴀɴ ᴀɴᴅ ᴇɴᴊᴏʏ ᴘʀᴇᴍɪᴜᴍ ᴍᴇᴍʙᴇʀꜱʜɪᴘ !

💵 ᴜᴘɪ ɪᴅ - <code>{}</code>

‼️ ᴍᴜsᴛ sᴇɴᴅ sᴄʀᴇᴇɴsʜᴏᴛ ᴀғᴛᴇʀ ᴘᴀʏᴍᴇɴᴛ.</b>"""

    QR_TXT = """<b>👋 ʜᴇʏ {},
    
 ᴘᴀʏ ᴀᴍᴍᴏᴜɴᴛ ᴀᴄᴄᴏʀᴅɪɴɢ ᴛᴏ ʏᴏᴜʀ ᴘʟᴀɴ ᴀɴᴅ ᴇɴᴊᴏʏ ᴘʀᴇᴍɪᴜᴍ ᴍᴇᴍʙᴇʀꜱʜɪᴘ !

📸 ǫʀ ᴄᴏᴅᴇ - <a href='{}'>ᴄʟɪᴄᴋ ʜᴇʀᴇ ᴛᴏ ꜱᴄᴀɴ</a>

‼️ ᴍᴜsᴛ sᴇɴᴅ sᴄʀᴇᴇɴsʜᴏᴛ ᴀғᴛᴇʀ ᴘᴀʏᴍᴇɴᴛ.</b>"""

    SOURCE_TXT ="""<b>ՏOᑌᖇᑕᗴ ᑕOᗪᗴ : 👇 </b>

This Is An Open-Source Project. You Can Use It Freely, But Selling The Source Code Is Strictly Prohibited.\n
ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ʜᴇʀᴇ ◉› :<a href=https://github.com/IQAnimes/Auto_Filter_Bot.git>IQAnime</a>\n """

    SETTING_TXT = """    
<u>ꜱᴇᴛᴛɪɴɢꜱ</u> :
- ꜱᴇᴛᴛɪɴɢꜱ ɪꜱ ᴛʜᴇ ᴍᴏꜱᴛ ɪᴍᴘᴏʀᴛᴀɴᴛ ꜰᴇᴀᴛᴜʀᴇ ᴏꜰ ᴛʜɪꜱ ʙᴏᴛ.
- ʏᴏᴜ ᴄᴀɴ ᴇᴀꜱɪʟʏ ᴄᴜꜱᴛᴏᴍɪᴢᴇ ᴛʜɪꜱ ʙᴏᴛ ꜰᴏʀ ʏᴏᴜʀ ɢʀᴏᴜᴘ.

<u>ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅꜱ</u> :
• /settings - ᴄʜᴀɴɢᴇ ᴛʜᴇ ɢʀᴏᴜᴘ ꜱᴇᴛᴛɪɴɢꜱ ᴀꜱ ʏᴏᴜʀ ᴡɪꜱʜ.
• /set_shortner - ꜱᴇᴛ ʏᴏᴜʀ 1ꜱᴛ ꜱʜᴏʀᴛɴᴇʀ.
• /set_shortner_2 - ꜱᴇᴛ ʏᴏᴜʀ 2ɴᴅ ꜱʜᴏʀᴛɴᴇʀ.
• /set_shortner_3 - ꜱᴇᴛ ʏᴏᴜʀ 3ʀᴅ ꜱʜᴏʀᴛɴᴇʀ.
• /set_tutorial - ꜱᴇᴛ ʏᴏᴜʀ 1ꜱᴛ ᴛᴜᴛᴏʀɪᴀʟ ᴠɪᴅᴇᴏ .
• /set_tutorial_2 - ꜱᴇᴛ ʏᴏᴜʀ 2ɴᴅ ᴛᴜᴛᴏʀɪᴀʟ ᴠɪᴅᴇᴏ .
• /set_tutorial_3 - ꜱᴇᴛ ʏᴏᴜʀ 3ʀᴅ ᴛᴜᴛᴏʀɪᴀʟ ᴠɪᴅᴇᴏ .
• /set_time - ꜱᴇᴛ 1ꜱᴛ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ ɢᴀᴘ.
• /set_time_2 - ꜱᴇᴛ 2ɴᴅ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ ɢᴀᴘ.
• /set_log_channel - ꜱᴇᴛ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ ʟᴏɢ ᴄʜᴀɴɴᴇʟ.
• /set_fsub - ꜱᴇᴛ ᴄᴜꜱᴛᴏᴍ ꜰᴏʀᴄᴇ ꜱᴜʙ ᴄʜᴀɴɴᴇʟ.
• /remove_fsub - ʀᴇᴍᴏᴠᴇ ᴄᴜꜱᴛᴏᴍ ꜰᴏʀᴄᴇ ꜱᴜʙ ᴄʜᴀɴɴᴇʟ.
• /reset_group - ʀᴇꜱᴇᴛ ʏᴏᴜʀ ꜱᴇᴛᴛɪɴɢꜱ.
• /details - ᴄʜᴇᴄᴋ ʏᴏᴜʀ ꜱᴇᴛᴛɪɴɢꜱ."""
    
    VERIFICATION_TEXT = """<b><i>👋 Oii {},

📌 ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴠᴇʀɪꜰɪᴇᴅ ᴛᴏᴅᴀʏ, ᴘʟᴇᴀꜱᴇ ᴄʟɪᴄᴋ ᴏɴ ᴠᴇʀɪꜰʏ & ɢᴇᴛ ᴜɴʟɪᴍɪᴛᴇᴅ ᴀᴄᴄᴇꜱꜱ ꜰᴏʀ ᴛɪʟʟ ɴᴇxᴛ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ.

#ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ:- 1/3 ✓

ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴅɪʀᴇᴄᴛ ꜰɪʟᴇs ᴛʜᴇɴ ʏᴏᴜ ᴄᴀɴ ᴛᴀᴋᴇ ᴘʀᴇᴍɪᴜᴍ sᴇʀᴠɪᴄᴇ (ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴠᴇʀɪꜰʏ).</i></b>"""
    

    VERIFY_COMPLETE_TEXT = """<b><i>👋 Oii {},

ʏᴏᴜ ʜᴀᴠᴇ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ᴛʜᴇ 1ꜱᴛ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ ✓

ɴᴏᴡ ʏᴏᴜ ʜᴀᴠᴇ ᴜɴʟɪᴍɪᴛᴇᴅ ᴀᴄᴄᴇss ꜰᴏʀ ɴᴇxᴛ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ.</i></b>"""

    SECOND_VERIFICATION_TEXT = """<b><i>👋 Oii {},

📌 ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴠᴇʀɪꜰɪᴇᴅ, ᴛᴀᴘ ᴏɴ ᴛʜᴇ ᴠᴇʀɪꜰʏ ʟɪɴᴋ ᴀɴᴅ ɢᴇᴛ ᴜɴʟɪᴍɪᴛᴇᴅ ᴀᴄᴄᴇss ꜰᴏʀ ᴛɪʟʟ ɴᴇxᴛ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ.

#ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ:- 2/3 ✓

ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴅɪʀᴇᴄᴛ ꜰɪʟᴇs ᴛʜᴇɴ ʏᴏᴜ ᴄᴀɴ ᴛᴀᴋᴇ ᴘʀᴇᴍɪᴜᴍ sᴇʀᴠɪᴄᴇ (ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴠᴇʀɪꜰʏ).</i></b>"""

    SECOND_VERIFY_COMPLETE_TEXT = """<b><i>👋 Oii {},
    
ʏᴏᴜ ʜᴀᴠᴇ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ᴛʜᴇ 2ɴᴅ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ ✓

ɴᴏᴡ ʏᴏᴜ ʜᴀᴠᴇ ᴜɴʟɪᴍɪᴛᴇᴅ ᴀᴄᴄᴇss ꜰᴏʀ ɴᴇxᴛ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ.</i></b>"""

    THIRDT_VERIFICATION_TEXT = """<b><i>👋 Oii {},
    
📌 ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴠᴇʀɪꜰɪᴇᴅ, ᴛᴀᴘ ᴏɴ ᴛʜᴇ ᴠᴇʀɪꜰʏ ʟɪɴᴋ & ɢᴇᴛ ᴜɴʟɪᴍɪᴛᴇᴅ ᴀᴄᴄᴇss ꜰᴏʀ ɴᴇxᴛ ꜰᴜʟʟ ᴅᴀʏ.</u>

#ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ:- 3/3 ✓

ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴅɪʀᴇᴄᴛ ꜰɪʟᴇs ᴛʜᴇɴ ʏᴏᴜ ᴄᴀɴ ᴛᴀᴋᴇ ᴘʀᴇᴍɪᴜᴍ sᴇʀᴠɪᴄᴇ (ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴠᴇʀɪꜰʏ)</i></b>"""

    THIRDT_VERIFY_COMPLETE_TEXT= """<b><i>👋 Oii {},
    
ʏᴏᴜ ʜᴀᴠᴇ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ᴛʜᴇ 3ʀᴅ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ ✓

ɴᴏᴡ ʏᴏᴜ ʜᴀᴠᴇ ᴜɴʟɪᴍɪᴛᴇᴅ ᴀᴄᴄᴇss ꜰᴏʀ ɴᴇxᴛ ꜰᴜʟʟ ᴅᴀʏ.</i></b>"""

    VERIFIED_LOG_TEXT = """ᴜꜱᴇʀ ᴠᴇʀɪꜰɪᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ✓

👤 Name:- {} [ <code>{}</code> ]

📆 Date:- <code>{} </code>

#Verificaton_{}_Completed"""


    ADMIN_CMD = """Oii 👋,

📚 ʜᴇʀᴇ ᴀʀᴇ ᴍʏ ᴄᴏᴍᴍᴀɴᴅꜱ ʟɪꜱᴛ ꜰᴏʀ ᴀʟʟ ʙᴏᴛ ᴀᴅᴍɪɴꜱ ⇊

• /start - <code>ᴛᴏ ᴜꜱᴇ ᴍʏ ꜰᴇᴀᴛᴜʀᴇꜱ.</code>
• /stats - <code>ɢᴇᴛ ᴛʜᴇ ᴛᴏᴛᴀʟ ᴜꜱᴇʀꜱ ᴀɴᴅ ᴄʜᴀᴛꜱ.</code>
• /del_msg - <code>ʀᴇᴍᴏᴠᴇ ғɪʟᴇ ɴᴀᴍᴇ ᴄᴏʟʟᴇᴄᴛɪᴏɴ ɴᴏтɪғɪᴄᴀᴛɪᴏɴ...</code>
• /movie_update - <code>ᴏɴ / ᴏғғ ᴀᴄᴄᴏʀᴅɪɴɢ ʏᴏᴜʀ ɴᴇᴇᴅᴇᴅ...</code> 
• /pm_search - <code>ᴘᴍ sᴇᴀʀᴄʜ ᴏɴ / ᴏғғ ᴀᴄᴄᴏʀᴅɪɴɢ ʏᴏᴜʀ ɴᴇᴇᴅᴇᴅ...</code>
• /verify - <code>ᴛᴜʀɴ ᴏɴ / ᴏꜰꜰ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ (ᴏɴʟʏ ᴡᴏʀᴋ ɪɴ ɢʀᴏᴜᴘ)</code>
• /logs - <code>ɢᴇᴛ ᴛʜᴇ ʀᴇᴄᴇɴᴛ ᴇʀʀᴏʀꜱ.</code>
• /delete - <code>ᴅᴇʟᴇᴛᴇ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ꜰɪʟᴇ ꜰʀᴏᴍ ᴅʙ.</code>
• /users - <code>ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴍʏ ᴜꜱᴇʀꜱ ᴀɴᴅ ɪᴅꜱ.</code>
• /chats - <code>ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴍʏ ᴄʜᴀᴛꜱ ᴀɴᴅ ɪᴅꜱ.</code>
• /leave  - <code>ʟᴇᴀᴠᴇ ꜰʀᴏᴍ ᴀ ᴄʜᴀᴛ.</code>
• /disable  -  <code>ᴅɪꜱᴀʙʟᴇ ᴀ ᴄʜᴀᴛ.</code>
• /ban  - <code>ʙᴀɴ ᴀ ᴜꜱᴇʀ.</code>
• /unban  - <code>ᴜɴʙᴀɴ ᴀ ᴜꜱᴇʀ.</code>
• /broadcast - <code>ʙʀᴏᴀᴅᴄᴀꜱᴛ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ᴀʟʟ ᴜꜱᴇʀꜱ.</code>
• /grp_broadcast - <code>ʙʀᴏᴀᴅᴄᴀsᴛ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴀʟʟ ᴄᴏɴɴᴇᴄᴛᴇᴅ ɢʀᴏᴜᴘs.</code>
• /deletefiles - <code>ᴅᴇʟᴇᴛᴇ CᴀᴍRɪᴘ ᴀɴᴅ PʀᴇDVD ғɪʟᴇs ғʀᴏᴍ ᴛʜᴇ ʙᴏᴛ's ᴅᴀᴛᴀʙᴀsᴇ.</code>
• /send - <code>ꜱᴇɴᴅ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴜꜱᴇʀ.</code>
• /add_premium - <code>ᴀᴅᴅ ᴀɴʏ ᴜꜱᴇʀ ᴛᴏ ᴘʀᴇᴍɪᴜᴍ.</code>
• /remove_premium - <code>ʀᴇᴍᴏᴠᴇ ᴀɴʏ ᴜꜱᴇʀ ꜰʀᴏᴍ ᴘʀᴇᴍɪᴜᴍ.</code>
• /premium_users - <code>ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴘʀᴇᴍɪᴜᴍ ᴜꜱᴇʀꜱ.</code>
• /get_premium - <code>ɢᴇᴛ ɪɴꜰᴏ ᴏꜰ ᴀɴʏ ᴘʀᴇᴍɪᴜᴍ ᴜꜱᴇʀ.</code>
• /restart - <code>ʀᴇꜱᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ.</code>"""

    GROUP_CMD = """Oii 👋,
📚 ʜᴇʀᴇ ᴀʀᴇ ᴍʏ ᴄᴏᴍᴍᴀɴᴅꜱ ʟɪꜱᴛ ꜰᴏʀ ᴄᴜꜱᴛᴏᴍɪᴢᴇᴅ ɢʀᴏᴜᴘꜱ ⇊

• /settings - ᴄʜᴀɴɢᴇ ᴛʜᴇ ɢʀᴏᴜᴘ ꜱᴇᴛᴛɪɴɢꜱ ᴀꜱ ʏᴏᴜʀ ᴡɪꜱʜ.
• /set_shortner - ꜱᴇᴛ ʏᴏᴜʀ 1ꜱᴛ ꜱʜᴏʀᴛɴᴇʀ.
• /set_shortner_2 - ꜱᴇᴛ ʏᴏᴜʀ 2ɴᴅ ꜱʜᴏʀᴛɴᴇʀ.
• /set_shortner_3 - ꜱᴇᴛ ʏᴏᴜʀ 3ʀᴅ ꜱʜᴏʀᴛɴᴇʀ.
• /set_tutorial - ꜱᴇᴛ ʏᴏᴜʀ 1ꜱᴛ ᴛᴜᴛᴏʀɪᴀʟ ᴠɪᴅᴇᴏ .
• /set_tutorial_2 - ꜱᴇᴛ ʏᴏᴜʀ 2ɴᴅ ᴛᴜᴛᴏʀɪᴀʟ ᴠɪᴅᴇᴏ .
• /set_tutorial_3 - ꜱᴇᴛ ʏᴏᴜʀ 3ʀᴅ ᴛᴜᴛᴏʀɪᴀʟ ᴠɪᴅᴇᴏ .
• /set_time - ꜱᴇᴛ 1ꜱᴛ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ ɢᴀᴘ.
• /set_time_2 - ꜱᴇᴛ 2ɴᴅ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ ɢᴀᴘ.
• /set_log_channel - ꜱᴇᴛ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ ʟᴏɢ ᴄʜᴀɴɴᴇʟ.
• /set_fsub - ꜱᴇᴛ ᴄᴜꜱᴛᴏᴍ ꜰᴏʀᴄᴇ ꜱᴜʙ ᴄʜᴀɴɴᴇʟ.
• /remove_fsub - ʀᴇᴍᴏᴠᴇ ᴄᴜꜱᴛᴏᴍ ꜰᴏʀᴄᴇ ꜱᴜʙ ᴄʜᴀɴɴᴇʟ.
• /reset_group - ʀᴇꜱᴇᴛ ʏᴏᴜʀ ꜱᴇᴛᴛɪɴɢꜱ.
• /details - ᴄʜᴇᴄᴋ ʏᴏᴜʀ ꜱᴇᴛᴛɪɴɢꜱ."""    



    
