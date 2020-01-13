**(\*) = same-user (user who ran the command)**

**(#) = needs hex code (Eg #db7991 or just db7991**

**(%) = user input (text)**

**($) = user input (attachment)**

**(@) = user mention**



**Profile commands**
-----
`#=profile create`

`#=profile addtext (%)`

`#=profile view (*)`

`#=profile background (#)`

`#=profile color (#)`

**Posting Commands**
-----
#=post create <ARGS>

  Arguments:
   `-noavatar` | will not show avatar next to name

   `-text(%)`  | text of post
   
   `-title(%)`  | title of post
 
   Note: the `-` and `()` are required.
      ``AT THE MOMENT IT WILL NOT BE PUBLIC!``
          I need to set up a webserver to communicate to my website & computer without sending data through AWS directly.
**API commands**
-----

  **Basic API commands**

    `#=neko  | random neko image from the NBAPI module. `

    `#=anime  | random anime image from the NBAPI module. `

    `#=pat | random pat image from the NBAPI module. `

  **Uploading to API**

    `#=neko upload ($) | only .png, .gif will use first frame visible, and will downscale the quality of the GIF.`

    `#=anime upload ($) | only .png, .gif will use first frame visible, and will downscale the quality of the GIF.`

    `#=pat upload ($) | auto detects .gif and .png apart`



