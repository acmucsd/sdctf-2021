# hIDe and seek
## Osint - Easy
| author | prereq chals | first blood | solves | final points |
| --- | --- | --- | --- | --- |
| KNOXDEV | none | **eris** from **Team IRS** | 89 | 100 |

### prompt
We don't know the flag, but we know some people who do! Here are their locations:

**Location 1**: ?v=hqXOIZtRYZU

**Location 2**: qFHIm0c.jpeg

### original specification
This challenge consists of some lookup IDs provided from many popular web platforms in no particular order and completely out of context, but are sufficient to find the post/video/user with the flag.
For example:
A Discord user ID (ie 71501943637282816) that can be looked up with https://discord.id/
A YouTube watch url: S-Lq4IB-5zk
Other ideas: imgur url, etc

**flag**: `sdctf{W0w_1_h4D_n0_ID3a!}`
### writeups
- https://hackmd.io/@ptr-yudai/BJ3BCl8dd#hIDe-and-seek
- https://github.com/thewhitecircle/ctf_writeups/blob/main/sdctf_2021/osint.md#hide-and-seek
- https://qiita.com/mikecat_mixc/items/5a0c45751b15c8a8513b#hide-and-seek
- https://github.com/sociallyencrypted/SDCTF2021-Writeups#hide-and-seek


# hIDe and seek 2
## Osint - Easy
| author | prereq chals | first blood | solves | final points |
| --- | --- | --- | --- | --- |
| KNOXDEV | hIDe and seek | **eris** from **Team IRS** | 57 | 200 |

### prompt
I've gotten some more good intel. Apparently, the following information is the location of another flag!

**Location 1**: gg/4KcDWnUYMs

**Location 2**: 810237829564727312-810359639975526490

### original specification
Unlocked once hIDe and seek 1 is completed. The two IDs this time are a discord server invite and a discord message ID. The invite drops you into a server with one channel with no message send permissions, and roughly 10000 messages with fake flags. The correct flag is the one indicated with the message ID.

**flag**: `sdctf{m@st3R_h@Ck3R_4807}`
### writeups
- https://hackmd.io/@ptr-yudai/BJ3BCl8dd#hIDe-and-seek-2
- https://github.com/thewhitecircle/ctf_writeups/blob/main/sdctf_2021/osint.md#hide-and-seek-2
- https://qiita.com/mikecat_mixc/items/5a0c45751b15c8a8513b#hide-and-seek-2
- https://github.com/sociallyencrypted/SDCTF2021-Writeups#hide-and-seek-2
