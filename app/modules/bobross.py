#import random, discord, asyncio
def pickRandomLine(name, icon, lines):
    randLine = random.randint(0, len(lines) - 1)
    line = lines[randLine]
    e = discord.Embed(description=line)
    e.set_author(name=name, icon_url=icon)
    return e

embedRossIcon = "http://i.imgur.com/OZLdaSn.png"

rossQuotes = ["There’s nothing wrong with having a tree as a friend.",
    "The secret to doing anything is believing that you can do it. Anything that you believe you can do strong enough, you can do. Anything. As long as you believe.",
    "We don’t make mistakes. We just have happy accidents.",
    "I think there’s an artist hidden at the bottom of every single one of us.",
    "You too can paint almighty pictures.",
    "No pressure. Just relax and watch it happen.",
    "Don’t forget to make all these little things individuals — all of them special in their own way.",
    "Find freedom on this canvas.",
    "It’s so important to do something every day that will make you happy.",
    "Talent is a pursued interest. Anything that you’re willing to practice, you can do.",
    "Make love to the canvas.",
    "[Painting] will bring a lot of good thoughts to your heart.",
    "We artists are a different breed of people. We’re a happy bunch.",
    "We want happy paintings. Happy paintings. If you want sad things, watch the news.",
    "That’s a crooked tree. We’ll send him to Washington.",
    "Every day is a good day when you paint.",
    "I think each of us, sometime in our life, has wanted to paint a picture.",
    "We tell people sometimes: We’re like drug dealers, come into town and get everybody absolutely addicted to painting. It doesn’t take much to get you addicted.",
    "They say everything looks better with odd numbers of things. But sometimes I put even numbers — just to upset the critics.",
    "Gotta give him a friend. Like I always say, ‘Everyone needs a friend.’",
    "See how it fades right into nothing. That’s just what you’re looking for.",
    "If I paint something, I don’t want to have to explain what it is.",
    "Water’s like me. It’s lazy. Boy, it always looks for the easiest way to do things.",
    "In painting, you have unlimited power. You have the ability to move mountains. You can bend rivers. But when I get home, the only thing I have power over is the garbage.",
    "Don’t forget to tell these special people in your life just how special they are to you.",
    "Didn’t you know you had that much power? You can move mountains. You can do anything.",
    "I like to beat the brush.",
    "Just let go — and fall like a little waterfall.",
    "Talk to the tree, make friends with it.",
    "I taught my son to paint mountains like these, and guess what? Now he paints the best darn mountains in the industry.",
    "I really believe that if you practice enough you could paint the ‘Mona Lisa’ with a two-inch brush.",
    "Be so very light. Be a gentle whisper.",
    "Use absolutely no pressure. Just like an angel’s wing.",
    "You need the dark in order to show the light.",
    "You can do anything you want to do. This is your world.",
    "You have to allow the paint to break to make it beautiful.",
    "However you think it should be, that’s exactly how it should be.",
    "In nature, dead trees are just as normal as live trees.",
    "You can have anything you want in the world — once you help everyone around you get what they want.",
    "If you do too much, it’s going to lose its effectiveness.",
    "This is happy place; little squirrels live here and play.",
    "That’s where the crows will sit. But we’ll have to put an elevator to put them up there because they can’t fly, but they don’t know that, so they still try.",
    "Remember how free clouds are. They just lay around in the sky all day long.",
    "We don’t really know where this goes — and I’m not sure we really care.",
    "If we’re going to have animals around we all have to be concerned about them and take care of them.",
    "You can do anything here — the only prerequisite is that it makes you happy.",
    "Go out on a limb — that’s where the fruit is.",
    "Isn’t it fantastic that you can change your mind and create all these happy things?",
    "Anytime you learn, you gain.",
    "It’s life. It’s interesting. It’s fun.",
    "Trees are like people. They all have a few flaws in them.",
    "When you get a little challenge in your life you tend to enjoy it.",
    "Even a little tree will grow up to be a big tree. All it needs is water, sunshine and love - the same as all of us.",
    "There’s tranquility and peace in my world, there’s never any violence.",
    "Art should make you feel good about yourself and about the world.",
    "It is my world and everything in my world is happy.",
    "If it ain’t broke, don’t fix it - but nothing is broken, so don’t worry about trying to fix anything.",
    "Let’s be brave - because we can do anything.",
    "We all have different ideas - and they’re all good - there is no good or bad.",
    "Think about a thunderstorm, they have a chaotic sound but when they are over everything is clean, fresh and beautiful again.",
    "The joy in life comes from doing your own thing.",
    "Go outside and make friends with a tree.",
    "Do a little, but don’t get greedy.",
    "All you have to do is decide and then let the rest happen.",
    "It will look like life is just exploding.",
    "At this point we’re not concerned - we’ll worry about that later.",
    "Just a tiny bit, we don’t need much today.",
    "If you look into the clouds long enough, you’ll find what you’re looking for.",
    "Too much will ruin the illusion.",
    "You just have to find what works for you.",
    "It’s a long way off, we don’t even know where it goes - but we don’t need to care.",
    "It gets to feel good and you want to just keep doing it, but the key is restraint.",
    "Once you get over the fear, you’ll be amazed at what you can do.",
    "Of course you can do that. You can do anything.",
    "Trees grow in every shape and size, just like people - and that’s what makes them fantastic.",
    "If you have to do something over again, it doesn’t mean you’re bad, it just means you’re normal.",
    "Let your imagination take you anywhere you want to go.",
    "If you don’t think you can do this - you’re not realizing how simple it is.",
    "Nothing in the world breeds success like success, even if you start with the smallest amount.",
    "There’s no good or bad. There’s just what makes you happy.",
    "It really doesn’t matter, we can always paint over it.",
    "Anything that you can visualize in your mind, you can do.",
    "Sometimes you can amaze yourself.",
    "All you have to do is realize there are no boundaries here.",
    "You can do anything in this life. As long as you believe you can.",
    "Sometimes life has a funny sense of humor.",
    "Once in awhile you need a little sorrow in your life.",
    "Don’t be afraid to go out on a limb. That’s where the fruit is.",
    "Spend some time talking with the trees.",
    "No one has ever been hurt by having too many friends.",
    "We don’t need to set the sky on fire, a little glow will do just fine.",
    "I love every little bird and critter.",
    "It can be scary to have this much power.",
    "Everybody has their own ideas, and that’s the way it should be.",
    "The only rule is that you should enjoy this.",
    "Remember, you can do anything in your world that you want to.",
    "All it takes is just a little change of perspective and you begin to see a whole new world.",
    "Everyone is going to see things differently - and that’s the way it should be.",
    "You can create beautiful things - but you have to see them in your mind first",
    "Don’t be afraid to make these big decisions. Once you start, they sort of just make themselves.",
    "With something so strong, a little bit can go a long way.",
    "Think about a cloud. Just float around and be there.",
    "In nature, dead trees are just as normal as live trees.",
    "You have to put some dark color in so your light color will show.",
    "In life you need colors.",
    "It’s a super day, so why not make a beautiful sky?",
    "It’s beautiful - and we haven’t even done anything to it yet",
    "Pretend you’re water. Just floating without any effort. Having a good day.",
    "They say everything looks better with odd numbers of things. But sometimes I put even numbers - just to upset the critics.",
    "When things happen - enjoy them. They’re little gifts.",
    "Take your time. Speed will come later.",
    "It’s amazing what you can do with a little love in your heart.",
    "God gave you this gift of imagination. Use it.",
    "You can do anything your heart can imagine.",
    "With practice comes confidence.",
    "If you don’t like it - change it. It’s your world.",
    "There is immense joy in just watching - watching all the little creatures in nature.",
    "That is when you can experience true joy, when you have no fear.",
    "We don’t really know where this goes - and I’m not sure we really care.",
    "Life is too short to be alone, too precious. Share it with a friend.",
    "If we’re going to have animals around we all have to be concerned about them and take care of them.",
    "Dead trees are also a part of nature.",
    "Sometimes you learn more from your mistakes than you do from your masterpieces.",
    "You want your tree to have some character. Make it special.",
    "The man who does the best job is the one who is happy at his job.",
    "Everything’s not great in life, but we can still find beauty in it.",
    "You’re the greatest thing that has ever been or ever will be. You’re special. You’re so very special.",
    "There are no accidents. There are no mistakes.",
    "There is no right or wrong - as long as it makes you happy and doesn’t hurt anyone.",
    "Everyone needs a friend. Friends are the most valuable things in the world.",
    "There are no mistakes. You can fix anything that happens.",
    "That’s why I paint - because I can create the kind of world I want - and I can make this world as happy as I want it.",
    "How do you make a round circle with a square knife? That’s your challenge for the day.",
    "Just think about these things in your mind - then bring them into your world."]
    