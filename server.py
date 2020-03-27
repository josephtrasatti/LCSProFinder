# coding=utf-8
from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

current_id = 4

players = [
	{
		"id": 1,
		"player": "Doublelift",
		"role": "ADC",
		"description": "\"Everyone else is trash\" - Doublelift. One of the greatest to every play the game."
					   "He has made it to Worlds more than anyone else in NA, however, his performance there is "
					   "less than to be desired. He has NEVER made it out of groups, but I believe, Doublelift will "
					   "save the world.",
		"age": 25,
		"teams": [{"team": "CLG", "deleted": False,}, {"team": "TSM", "deleted": False,}, {"team": "TL", "deleted": False,}],
		"picture": "https://lolstatic-a.akamaihd.net/esports-assets/production/player/doublelift-igod502r.png",
		"scene": "pro",
	},
	{
		"id": 2,
		"player": "Wildturtle",
		"role": "ADC",
		"description": "Known for earning a penta kill in his first game, he has been around for years now. "
					   "Wildturtle is a humble player, who always puts his team first. He has been a staple on every"
					   "team he plays on, known for both his consistency and play making ability. He is a fan favorite.",
		"age": 26,
		"teams": [{"team": "TSM", "deleted": False,}, {"team": "IMT", "deleted": False,}, {"team": "FLY", "deleted": False,}],
		"picture": "https://gamepedia.cursecdn.com/lolesports_gamepedia_en/7/79/FLY_WildTurtle_2020_Split_1.png",
		"scene": "pro",
	},
	{
		"id": 3,
		"player": "Sneaky",
		"role": "ADC",
		"description": "The meme king - \"sneaky in lane phase\". Has had the most international "
					   "success of any North American Team. Sneaky has a hobby of cosplay, and has always been a man"
					   "of the people. He is also known for his ability to discover bugs, as well as his meme "
					   "knowledge.",
		"age": 25,
		"teams": [{"team": "C9", "deleted": False,},],
		"picture": "https://gamepedia.cursecdn.com/lolesports_gamepedia_en/3/32/2019_Allstars_Sneaky.png",
		"scene": "pro",
		"deleted": False,
	},
	{
		"id": 4,
		"player": "Voyboy",
		"role": "Mid",
		"description": "Now, Voyboy is no more than a simple streamer. However, back in the day, his assassin skills "
					   "were unmatched. Voyboy has done many charity events and has one of the biggest hearts of anyone."
					   "His laugh is contagious, and his skills are outrageous.",
		"age": 27,
		"teams": [{"team": "Curse", "deleted": False,}],
		"picture": "https://gamepedia.cursecdn.com/lolesports_gamepedia_en/0/07/NA_Voyboy_2018_AS.png",
		"scene": "retired_pro",
		"deleted": False,
	},
	{
		"id": 5,
		"player": "Faker",
		"role": "Mid",
		"description": "Often considered the true greatest of all time... faker faker play-maker. "
					   "Has 3 world championships under his belt, and his skills are truly above everyone else's."
					   "He has only every played for one team, and that team has in return given all its "
					   "recourse's to him. He also managers to be a selfless player at the same time as he "
					   "carries the team on his back.",
		"age": 27,
		"teams": [{"team": "SKT", "deleted": False,}],
		"picture": "https://gamepedia.cursecdn.com/lolesports_gamepedia_en/7/71/T1_Faker_2020_Split_1.png",
		"scene": "pro",
		"deleted": False,
	},
	{
		"id": 6,
		"player": "Pobelter",
		"role": "Mid",
		"description": "Pobelter has played since the beginning when he was barely old enough to play professionally."
					   " He has so much experience under his belt and has yet to see his best days. Pobelter is known"
					   "for doing a lot with little recourse's, making him a very valuable asset to the team. Any team"
					   "would be lucky to pick him us as their star mid laner.",
		"age": 23,
		"teams": [{"team": "CLG", "deleted": False,}, {"team": "TL", "deleted": False,}],
		"picture": "https://www.esportspedia.com/lol/images/2/22/FLY_Pobelter_2019_Summer.png",
		"scene": "pro",
		"deleted": False,
	},
	{
		"id": 7,
		"player": "Impact",
		"role": "Top",
		"description": "\"Top die\" - an iconic line from a world champion. Impact is a man of few words,"
					   " but big plays. He can play any top laner in any meta. Impact has an amazing work ethic and "
					   "he constantly strives for improvement.",
		"age": 24,
		"teams": [{"team": "SKT", "deleted": False,}, {"team": "C9", "deleted": False,}, {"team": "TL", "deleted": False,}],
		"picture": "https://www.esportspedia.com/lol/thumb.php?f=C9-Impact-2017.png&width=227",
		"scene": "pro",
		"deleted": False,
	},
	{
		"id": 8,
		"player": "Bjergsen",
		"role": "Mid",
		"description": "Many would say Bjergsen is the greatest player from NA. He has made it worlds"
					   " almost every year, and has played well internationally too. Bjerg is a legend amoung men"
					   " and his reign is far from over. One day, he will make it to the grand stage.",
		"age": 24,
		"teams": [{"team": "TSM", "deleted": False,}],
		"picture": "https://gamepedia.cursecdn.com/lolesports_gamepedia_en/9/98/TSM_Bjergsen_2020_Split_1.png",
		"scene": "pro",
		"deleted": False,
	},
	{
		"id": 9,
		"player": "Imaqtpie",
		"role": "ADC",
		"description": "The meme legend - the best ADC in the world. QTPie is a former pro player who was just too "
					   "good for the game. So he quit and become the most entertaining streamer on twitch."
					   "He makes millions a year but deserves billions. ",
		"age": 30,
		"teams": [{"team": "DIG", "deleted": False,}],
		"picture": "https://gamepedia.cursecdn.com/lolesports_gamepedia_en/1/11/NA_Imaqtpie_2018_AS.png",
		"scene": "retired_pro",
		"deleted": False,
	},
	{
		"id": 10,
		"player": "XPeke",
		"role": "Mid",
		"description": "The man literally has a move named after him. So many iconic moments and great plays."
					   "It pains me to speak so highly of a EU player, but it is truly deserved."
					   "Fnatic has made itself a legacy thanks to his work, and his end is no where near to come.",
		"age": 27,
		"teams": [{"team": "FNC", "deleted": False,}],
		"picture": "https://lolstatic-a.akamaihd.net/esports-assets/production/player/xpeke-8f3dmcvw.png",
		"scene": "pro",
		"deleted": False,
	},
	{
		"id": 11,
		"player": "Meteos",
		"role": "JG",
		"description": "Although born in Massachusetts, Meteos' hometown is actually Fairfax, Virginia. "
					   "He started playing games around the age of 5 with his mother's Game Boy. "
					   "Before League of Legends, he was a sophomore at Christopher Newport University working towards "
					   "a degree in Computer Science. When the beta for LoL came out, Meteos and his "
					   "friends only played normal games.",
		"age": 26,
		"teams": [{"team": "C9", "deleted": False,}],
		"picture": "https://gamepedia.cursecdn.com/lolesports_gamepedia_en/0/09/100_Meteos_2020_Split_1.png",
		"scene": "retired_pro",
		"deleted": False,
	},
	{
		"id": 12,
		"player": "Zven",
		"role": "ADC",
		"description": "He started playing video games with World of Warcraft at the age of 12. "
					   "He eventually started playing League of Legends because his teacher at primary school "
					   "introduced him to the game. "
					   "He is still currently in school, as he strives to become a computer programmer in the future."
					   "He had a very tough first season in NA, however, he is performing better on C9 this year.s",
		"age": 22,
		"teams": [{"team": "TSM", "deleted": False,}, {"team": "C9", "deleted": False,}],
		"picture": "https://www.esportspedia.com/lol/images/4/4a/TSM_Zven_2019_Summer.png",
		"scene": "pro",
		"deleted": False,
	},
	{
		"id": 13,
		"player": "Scarra",
		"role": "Mid, JG",
		"description": "William \"scarra\" Li is a League of Legends esports player, currently streamer for Offline TV. "
					   "He is best known for being the mid laner for Team Dignitas. He is now the owner and coach of "
					   "Dignitas and has done wonders for the team. He is also known for his time in the "
					   "amateur league on the stream dream team.",
		"age": 30,
		"teams": [{"team": "DIG", "deleted": False,}],
		"picture": "https://lolstatic-a.akamaihd.net/esports-assets/production/player/scarra-5x01i56g.png",
		"scene": "retired_pro",
		"deleted": False,
	},
	{
		"id": 14,
		"player": "Huni",
		"role": "Top",
		"description": "Huni started his career on Samsung Gaming and made a big debut. After playing on SKT, he "
					   "decided to move to NA for those sweet deals. ",
		"age": 22,
		"teams": [{"team": "SG", "deleted": False,}, {"team": "IMT", "deleted": False,}, {"team": "SKT", "deleted": False,},
		 {"team": "FNC", "deleted": False,}, {"team": "CG", "deleted": False,}, {"team": "DIG", "deleted": False,},],
		"picture": "https://www.esportspedia.com/lol/images/b/bd/CG_Huni_2019_Spring.png",
		"scene": "pro",
		"deleted": False,
	},
	{
		"id": 15,
		"player": "Froggen",
		"role": "Mid",
		"description": "Since his childhood, Henrik “Froggen” Hansen has played video games such as Counter-Strike "
					   "and Warcraft 3. Froggen then started playing League. Froggen had unrivealed mechanics which"
					   "allowed him to play with the best. Mechanics and lane dominance are two aspects of Froggen’s "
					   "gameplay that he believes will set him above the rest, and secure victories for his team.",
		"age": 26,
		"teams": [{"team": "EF", "deleted": False,}, {"team": "OG", "deleted": False,}, {"team": "GG", "deleted": False,},
		 {"team": "DIG", "deleted": False,},],
		"picture": "https://gamepedia.cursecdn.com/lolesports_gamepedia_en/9/9b/DIG_Froggen_2020_Split_1.png",
		"scene": "pro",
		"deleted": False,
	},
	{
		"id": 16,
		"player": "Xmithie",
		"role": "JG",
		"description": "Xmithie was born and raised in the Philippines. When Jake was 16, his family decided to move "
					   "to the United States. Jake began playing video games at an early age, as his father owned a "
					   "computer shop that also contained PlayStation consoles and games. Xmithie's gaming history "
					   "began at the age of 6, originally playing on the famicom before moving on to the Gameboy and "
					   "then PlayStation 1.",
		"age": 28,
		"teams": [{"team": "CLG", "deleted": False,}, {"team": "TL", "deleted": False,}, {"team": "IMT", "deleted": False,}],
		"picture": "https://www.esportspedia.com/lol/images/4/4a/TL_Xmithie_2019_Spring.png",
		"scene": "pro",
		"deleted": False,
	},
	{
		"id": 17,
		"player": "Jensen",
		"role": "Mid",
		"description": "Jensen is a Danish player who is currently playing on TL in NA. He has made it to worlds "
					   "almost every season he has played. Jensen has amazing mechanics but even better "
					   "team play. He has many more years ahead of him and hopes to one day hold the "
					   "champion trophy.",
		"age": 25,
		"teams": [{"team": "C9", "deleted": False,}, {"team": "TL", "deleted": False,}],
		"picture": "https://www.esportspedia.com/lol/images/d/d4/TL_Jensen_2019_Spring.png",
		"scene": "pro",
		"deleted": False,
	},
	{
		"id": 18,
		"player": "PowerOfEvil",
		"role": "Mid",
		"description": "PowerOfEvil is from Bad Soden, Germany. He started playing videos games as a kid, spending "
					   "time with titles like Warcraft III and Age of Empires 2. He is currently attending school at "
					   "Taunus gymnasium. Prior to playing competitively, he had aspirations of becoming a pilot and "
					   "flying internationally.",
		"age": 22,
		"teams": [{"team": "CLG", "deleted": False,}, {"team": "FLY", "deleted": False,}],
		"picture": "https://www.esportspedia.com/lol/images/7/7b/CLG_PowerOfEvil_2019_Summer.png",
		"scene": "pro",
		"deleted": False,
	},
	{
		"id": 19,
		"player": "Bang",
		"role": "ADC",
		"description": "Bang is a former world champion who started his career on SKT. Bang then decided to come to "
					   "NA to make the big bucks. Bang has elite mechanics, however, he has not been able to "
					   "perform as well since he has moved to NA. Hopefully, Bang will be able to make his glorious"
					   "comeback once again.",
		"age": 22,
		"teams": [{"team": "SKT", "deleted": False,}, {"team": "EG", "deleted": False,}],
		"picture": "https://www.esportspedia.com/lol/images/4/47/100_Bang_2019_Spring.png",
		"scene": "pro",
		"deleted": False,
	},
	{
		"id": 20,
		"player": "Santorin",
		"role": "JG",
		"description": "Santorin was one of the first of many TSM junglers. Santorin started playing video games when "
					   "he was 4-5 years old. Before he went to League of Legends, he was a football player and a "
					   "very good Counter Strike player. His League of Legends career started when he was searching "
					   "for something new, after he got tired of Counter Strike, this was part way through season 2.",
		"age": 22,
		"teams": [{"team": "TSM", "deleted": False,}, {"team": "FLY", "deleted": False,}],
		"picture": "https://gamepedia.cursecdn.com/lolesports_gamepedia_en/a/a7/NRG_Santorin_2016_Summer.png",
		"scene": "pro",
		"deleted": False,
	},
	{
		"id": 21,
		"player": "Traslinky",
		"role": "ADC JG",
		"description": "The man... the myth... the legend. Traslinky stats speak for themselves. 3 baron steals in "
					   "8 games and carry performances routinely. As captain of the PC esports team, traslinky led"
					   "his team into battle routinely. Traslinky, while low on the rank ladder, competed and beat "
					   "many far above him. His skills know no bounds. ",
		"age": 21,
		"teams": [{"team": "PC", "deleted": False,}],
		"picture": "https://pbs.twimg.com/media/Dx9Lom3V4AAwoNR.jpg",
		"scene": "collegiate",
		"deleted": False,
	},
	{
		"id": 22,
		"player": "Doopty",
		"role": "Supp Top",
		"description": "The #1 blitzcrank in the big east, and #1 in our hearts. Doopty's primary role is support, "
					   "however, when duty calls, he took up top lane to fight against the best. He competed "
					   "with challengers and beat them. His yorik was unstoppable, and his legacy is forever. Doopty "
					   "was on PC's original roster, some say thier best.",
		"age": 21,
		"teams": [{"team": "PC", "deleted": False,}],
		"picture": "https://gamepedia.cursecdn.com/lolesports_gamepedia_en/thumb/9/92/Doopty.jpeg/1200px-Doopty.jpeg",
		"scene": "collegiate",
		"deleted": False,
	},
	{
		"id": 23,
		"player": "Beady",
		"role": "JG",
		"description": "Beady was a new comer to league of legends when the big east tournament started. That did "
					   "not stop him from quickly learning the game to reach a high level of play. Beady is known for "
					   "his mechanical abilities however his game knowledge often lacked. Though he made up for it "
					   "with communication and hard work.",
		"age": 21,
		"teams": [{"team": "PC", "deleted": False,}],
		"picture": "https://news.providence.edu/files/2019/10/mcguanweb-714x1024.jpg",
		"scene": "collegiate",
		"deleted": False,
	},
	{
		"id": 24,
		"player": "Idette",
		"role": "Supp",
		"description": "Idette is Providence College's first and only woman gamer. This did not stop her from "
					   "being an absolute force in the game. Her skills are sharp and her game play is even "
					   "sharper. Idette studies computer science and grew up in Providence.",
		"age": 21,
		"teams": [{"team": "PC", "deleted": False,}],
		"picture": "https://news.providence.edu/files/2019/10/monterrozaweb-696x1024.jpg",
		"scene": "collegiate",
		"deleted": False,
	},
	{
		"id": 25,
		"player": "Kidmims",
		"role": "Overwatch",
		"description": "Ahmad Mims is probably the highest rank player at providence college. He has played on a "
					   "semi pro team, and his skills are absurd. He has the best mechanical skills there are, "
					   "and he has a great team mindset. Mims is a great gift to Providence College, and his "
					   "skills will not go unused.",
		"age": 20,
		"teams": [{"team": "PC", "deleted": False,}],
		"picture": "https://news.providence.edu/files/2019/10/mimsweb-678x1024.jpg",

		"scene": "collegiate",
		"deleted": False,
	},
	{
		"id": 26,
		"player": "KiWiKiD",
		"role": "Supp",
		"description": "Kiwikid was part of the original dig team that was known for its amazing play and "
					   "outrageous skills. They had the best baron calls, and many say, that it was Kiwi behind "
					   "the scenes making the calls. Kiwi will go down as not only a meme king, but the baron "
					   "play call GOD.",
		"age": 26,
		"teams": [{"team": "DIG", "deleted": False,}],
		"picture": "https://gamepedia.cursecdn.com/lolesports_gamepedia_en/1/1c/NRG_Kiwikid_2016_Summer.png",
		"scene": "retired_pro",
		"deleted": False,
	},
	{
		"id": 27,
		"player": "Zion Spartan",
		"role": "Top",
		"description": "Zion was also part of the original dig squad. He may be best known for his legendary Nasus "
					   "performance in playoffs against TSM where he backdoored the game. Zion temporarily changed "
					   "his name to Darshan to seem more professional, however he soon came back to his original "
					   "name of Zion Spartan. Zion stands for the little man, but when he presses R on nasus, "
					   "he is no longer a little man.",
		"age": 26,
		"teams": [{"team": "DIG", "deleted": False,}, {"team": "CLG", "deleted": False,}],
		"picture": "https://gamepedia.cursecdn.com/lolesports_gamepedia_en/1/1c/NRG_Kiwikid_2016_Summer.png",
		"scene": "pro",
		"deleted": False,
	},
	{
		"id": 28,
		"player": "Quas",
		"role": "Top",
		"description": "Quas grew up in Latin America playing on NA servers with a dream to go pro. Quas, being so "
					   "far from the server, playing on very high ping, but still managed to climb the ladder to prove "
					   "his skills. He performed well on curse, but had a tough time finding a new team afterwards. "
					   "He will always hold a place in our hearts for his underdog story.",
		"age": 26,
		"teams": [{"team": "Curse", "deleted": False,}],
		"picture": "https://gamepedia.cursecdn.com/lolesports_gamepedia_en/f/fd/TS_Quas_2017_Summer.png",
		"scene": "retired_pro",
		"deleted": False,
	},
	{
		"id": 29,
		"player": "IWillDominate",
		"role": "JG",
		"description": "Dom is known for his quick temper and quick reaction time. Dom only ever played for team "
					   "liquid, and although his skills were great, his ability to play with others was not quite "
					   "there. For that he reason, many teams were hesitant to take the risk on him. Now, Dom streams, "
					   "and he still rages, and gets banned pretty often.",
		"age": 29,
		"teams": [{"team": "Curse", "deleted": False,}],
		"picture": "https://gamepedia.cursecdn.com/lolesports_gamepedia_en/a/a5/TL_IWDominate_2016_Spring.png",
		"scene": "retired_pro",
		"deleted": False,
	},
	{
		"id": 30,
		"player": "Aphromoo",
		"role": "Supp",
		"description": "Aphromoo played on several teams starting in 2011. He began to gain recognition as the AD "
					   "Carry player of v8 eSports, where he played with PhantomL0rd, Muffinqt, and Unstoppable, "
					   "among others. He and Muffinqt were known as a strong duo lane and would play together again "
					   "on mTw.NA, mMe Ferus, and Team FeaR. During this time, he gained huge popularity as a "
					   "streamer. In December 2012, Aphromoo asked his viewers if they would still watch him play "
					   "if he switched his role to support; he then joined Counter Logic Gaming as their support "
					   "player.",
		"age": 27,
		"teams": [{"team": "CLG", "deleted": False,}, {"team": "DIG", "deleted": False,}],
		"picture": "https://gamepedia.cursecdn.com/lolesports_gamepedia_en/a/ac/DIG_aphromoo_2020_Split_1.png",
		"scene": "pro",
		"deleted": False,
	},
]

next_id = 31

@app.route('/')
def home():
	global players
	return render_template('home.html', matches=players[:12], search='@@@@@@@')

	

@app.route('/search')
def search():
	global players

	search = request.args.get('player')

	players_found = []
	
	for player in players:
		if (search.lower() in player['player'].lower() or search.lower() in player['role'].lower()):
			players_found.append(player)
	print(search)
	return render_template('search.html', matches=players_found, search=search.lower())

@app.route('/view/<id>')
def view_id(id=None):
	id_num = int(id)
	player_picked = None
	for player in players:
		if player["id"] == id_num:
			player_picked = player
	player_name = player_picked['player']
	player_picture = player_picked['picture']
	player_description = player_picked['description']
	player_age = player_picked['age']
	player_teams = player_picked['teams']
	player_role = player_picked['role']
	return render_template('view.html', player_name=player_name, player_picture=player_picture, 
	player_description=player_description, player_age=player_age, player_teams=player_teams, player_role=player_role, id_num=id_num)

@app.route('/delete_player', methods=['GET', 'POST'])
def delete_player():
	global players
	player_removed = None
	id = request.get_json()
	for i in range(len(players)):		
		if players[i]["id"] == id:
			player_removed = players.pop(i)
			print(player_removed)
			break
	return jsonify(player_removed=player_removed)
	

@app.route('/create')
def create():
	return render_template('create.html')

@app.route('/create_player', methods=['GET', 'POST'])
def create_player():
	global players
	global next_id
	
	json_data = request.get_json()

	name = json_data["player_name"]
	role = json_data["player_role"]
	description = json_data["player_description"]
	age = json_data["player_age"]
	team = json_data["player_teams"]
	image = json_data["player_image"]

	players.append({
		"id": next_id,
		"player": name,
		"role": role,
		"description": description,
		"age": age,
		"teams": team,
		"picture": image,
	})
	old_id=next_id

	next_id += 1

	return jsonify(old_id=old_id)

@app.route('/edit/<id>')
def edit(id):
	id_num = int(id)
	player_age = 0
	for player in players:
		if player["id"] == id_num:
			player_age = player["age"]
	return render_template('edit.html', player_age=player_age, id_num=id_num)

@app.route('/view/update_role',  methods=['GET', 'POST'])
def update_role():
	global players
	json_data = request.get_json()
	new_role = json_data["new_role"]
	id = int(json_data["id"])
	for player in players:
		if id == player["id"]:
			player["role"] = new_role
	return jsonify(player=player)

@app.route('/view/update_age',  methods=['GET', 'POST'])
def update_age():
	global players
	json_data = request.get_json()
	new_age = json_data["new_age"]
	id = int(json_data["id"])
	for player in players:
		if id == player["id"]:
			player["age"] = new_age
	return jsonify(player=player)

@app.route('/view/update_teams',  methods=['GET', 'POST'])
def update_teams():
	global players
	json_data = request.get_json()
	new_teams = json_data["new_teams"]
	id = int(json_data["id"])
	for player in players:
		if id == player["id"]:
			player["teams"] = new_teams
	return jsonify(player=player)

@app.route('/mark_as_deleted', methods=['GET', 'POST'])
def mark_as_deleted():
	global players
	json_data = request.get_json()
	id = int(json_data['id'])
	team_index = int(json_data['team_index'])
	team = None
	for player in players:
		if player["id"] == id:
			player["teams"][team_index]["deleted"] = True
			team = player["teams"][team_index]["team"]
	
	return jsonify(team=team)

@app.route('/undo_mark_as_deleted', methods=['GET', 'POST'])
def undo_mark_as_deleted():
	global players
	json_data = request.get_json()
	id = int(json_data['id'])
	team_name = json_data['team']
	print(team_name)
	for player in players:
		if player["id"] == id:
			for team in player["teams"]:
				if team['team'] == team_name:
					team["deleted"] = False
	
	return jsonify(player=player)


if __name__ == '__main__':
	app.run(debug = True)