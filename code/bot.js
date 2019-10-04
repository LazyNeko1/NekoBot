//is not yet made. Still need a api using js

//Right now, i'm just going to use the raw API data. /shrug
//obviously requires the dependincies below
const Discord = require('discord.js')


//end of dependincies
const client = new Discord.Client()





//this may not work, im still testing it












client.on('message', (receivedMessage) => {
    // Prevent bot from responding to its own messages
    if (receivedMessage.author == client.user) {
        return
    }

const nekoEmbed = new Discord.RichEmbed()
	.setTitle('Nekos!')
	.setImage(nbapi.random.neko())
	.setFooter('Made by LazyNeko', 'http://neko-bot.net/images/ownerimg.round.png');
    receivedMessage.channel.send(nekoEmbed)
})



client.login('')
