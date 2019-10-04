//is not yet made. Still need a api using js

//Right now, i'm just going to use the raw API data. /shrug
//obviously requires the dependincies below
const Discord = require('discord.js')
//const nbapi=require("nbapi")
var prefix = "#="
//end of dependincies
const client = new Discord.Client()





//this may not work, im still testing it












client.on('message', (receivedMessage) => {
    // Prevent bot from responding to its own messages
    if (receivedMessage.author == client.user) {
        return
    }

const animeEmbed = new Discord.RichEmbed()
	.setTitle('Anime!!')
	.setImage("http://neko-bot.net/anime/anime30.png")//nbapi.random.neko())//lib not ready
	.setFooter('Made by LazyNeko', 'http://neko-bot.net/images/ownerimg.round.png');
const nekoEmbed = new Discord.RichEmbed()
	.setTitle('Nekos!')
	.setImage("http://neko-bot.net/nekos/neko30.png")//nbapi.random.neko())//lib not ready
	.setFooter('Made by LazyNeko', 'http://neko-bot.net/images/ownerimg.round.png');
	if (receivedMessage.content.startsWith(prefix+"neko")){
    receivedMessage.channel.send(nekoEmbed)
}})



client.login("")
