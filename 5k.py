from getWordsForTranslation import ReadDocx

learned = ReadDocx()

list5k = ['the', 'to', 'it', 'and', 'that', 'of', 'is', 'in', 'what', 'we', 'me', 'this', 'he', 'for', 'my', 'on', 'have', 'your', 'do', 'was', 'no', 'not', 'be', 'are', 'don', 'know', 'can', 'but', 'all', 'so', 'just', 'here', 'they', 'like', 'get', 'she', 'if', 
'right', 'out', 'about', 'up', 'at', 'him', 'now', 'oh', 'one', 'come', 'well', 'her', 'how', 'yeah', 'will', 'got', 'want', 'think', 'as', 'see', 'did', 'good', 'who', 'from', 'let', 'his', 'yes', 'when', 'going', 'time', 'an', 'okay', 'look', 'us', 'would', 'them', 'where', 'were', 'take', 'then', 'had', 'or', 'been', 'our', 'gonna', 'really', 'man', 'some', 'say', 'hey', 'could', 'didn', 'by', 'need', 'something', 'has', 'too', 'more', 'way', 'down', 'make', 'very', 'never', 'only', 'people', 'over', 'little', 'please', 'love', 'should', 'mean', 'said', 'sorry', 'give', 'off', 'am', 'thank', 'any', 'two', 'doing', 'sure', 'thing', 'these', 'help', 'first', 'into', 'anything', 'still', 'find', 'life', 'nothing', 'sir', 'day', 'god', 'their', 'uh', 'must', 'other', 'wait', 'stop', 'call', 'won', 'away', 'than', 'thought', 'night', 'put', 'great', 'those', 'last', 'better', 'everything', 'told', 'mr.', 'new', 'things', 'always', 'keep', 'years', 'leave', 'does', 'money', 'around', 'doesn', 'name', 'place', 'ever', 'guys', 'father', 'guy', 'made', 'old', 'isn', 'lot', 'done', 'hello', 'nice', 'believe', 'girl', 'someone', 'fine', 'thanks', 'wanted', 'coming', 'every', 'ok', 'through', 'being', 'course', 'left', 'dad', 'enough', 'happened', 'came', 'may', 'mother', 'wrong', 'world', 'bad', 'might', 'three', 'today', 'another', 'understand', 'remember', 'ask', 'own', 'same', 'show', 'else', 'kill', 'talking', 'found', 'next', 'getting', 'care', 'car', 'looking', 'son', 'try', 'woman', 'went', 'hi', 'dead', 'many', 'mind', 'wasn', 'friend', 'best', 'mom', 'hell', 'morning', 'trying', 'boy', 'yourself', 'job', 'saw', 'family', 'real', 'without', 'baby', 'wouldn', 'move', 'most', 'seen', 'live', 'miss', 'actually', 'huh', 'shit', 'both', 'heard', 'once', 'ready', 'called', 'used', 'idea', 'knew', 'door', 'such', 'fuck', 'brother', 'also', 'pretty', 'bit', 'took', 'haven', 'yet', 'men', 'start', 'use', 'since', 'wife', 'days', 'tomorrow', 'matter', 'meet', 'tonight', 'everyone', 'run', 'wanna', 'ah', 'alone', 'myself', 'school', 'gone', 'um', 'end', 'saying', 'phone', 'play', 'looks', 'couldn', 
'fucking', 'problem', 'few', 'friends', 'gotta', 'open', 'anyone', 'killed', 'hope', 
'face', 'until', 'lost', 'police', 'excuse', 'turn', 'business', 'wants', 'says', 'true', 'die', 'heart', 'soon', 'each', 'worry', 'later', 'year', 'watch', 'music', 'hand', 'having', 'probably', 'doctor', 'sit', 'thinking', 'young', 'second', 'working', 
'person', 'kids', 'late', 'stuff', 'exactly', 'under', 'death', 'minute', 'pay', 'crazy', 'forget', 'everybody', 'kid', 'change', 'gave', 'happen', 'damn', 'five', 'drink', 'knows', 'its', 'whatever', 'eyes', 'shut', 'aren', 'hit', 'taking', 'easy', 'times', 'check', 'hands', 'minutes', 'deal', 'different', 'means', 'point', 'makes', 'asked', 'somebody', 'mine', 'making', 'body', 'afraid', 'sleep', 'chance', 'dear', 'four', 'anyway', 'close', 'ain', 'party', 'fun', 'word', 'comes', 'important', 'set', 'shall', 'story', 'number', 'daughter', 'least', 'waiting', 'hurt', 'moment', 'fight', 'week', 'husband', 'girls', 'rest', 'married', 'fire', 'game', 'nobody', 'mr', 'children', 'side', 'stand', 'read', 'though', 'cut', 'started', 'sister', 'supposed', 'between', 'child', 'goes', 'hours', 'women', 'almost', 'truth', 'able', 'lady', 'anymore', 'playing', 'gets', 'shot', 'reason', 'trouble', 'break', 'war', 'city', 'town', 'trust', 'dr.', 'met', 'office', 'question', 'brought', 'yours', 'welcome', 'high', 'wow', 'couple', 'died', 'free', 'either', 'seems', 'power', 'whoa', 'bye', 'buy', 'telling', 'tried', 'team', 'answer', 'gun', 'boys', 'line', 'news', 'hurry', 'months', 'sometimes', 'become', 'along', 'hate', 'food', 'needs', 'country', 'em', 'fact', 'lord', 'captain', 'six', 'funny', 'black', 'mrs.', 'alive', 'pick', 'feeling', 'living', 'cause', 'ahead', 'lose', 'king', 'plan', 'dinner', 'sighs', 'sort', 'leaving', 'shouldn', 'running', 'boss', 'alright', 'promise', 'taken', 'ma', 'book', 'sent', 'white', 'hour', 'anybody', 'small', 'perfect', 'lives', 'special', 'parents', 'john', 'himself', 'perhaps', 'sounds', 'serious', 'sick', 'company', 'ha', 'scared', 'uncle', 'red', 'possible', 'shoot', 'touch', 'sound', 'top', 'ass', 'laughs', 'cannot', 'asking', 'win', 'glad', 'control', 'hmm', 'human', 'drive', 'jack', 'bitch', 'luck', 'murder', 'happens', 'ten', 'daddy', 'finally', 'chuckles', 'seem', 'laughing', 'words', 'hospital', 'street', 'hang', 'dance', 'meeting', 'till', 'others', 'follow', 'sense', 'sex', 'lie', 'evening', 'master', 'known', 'dream', 'write', 'million', 'voice', 'sweet', 'rather', 'felt', 'lucky', 'somewhere', 'bet', 'jesus', 'longer', 'calling', 'worked', 'looked', 'less', 'pull', 'beat', 'careful', 'return', 'secret', 'weeks', 'weren', 'date', 'seeing', 'fall', 'given', 'ooh', 'straight', 'takes', 'song', 'future', 
'gentlemen', 'loved', 'changed', 'road', 'calm', 'wonderful', 'turned', 'drop', 'ladies', 'learn', 'absolutely', 'early', 'explain', 'piece', 'yesterday', 'picture', 'feet', 'wonder', 'questions', 'speaking', 'worth', 'darling', 'dude', 'giving', 'president', 'quick', 'moving', 'figure', 'state', 'sam', 'none', 'amazing', 'ones', 'works', 'act', 'needed', 'law', 'worried', 'report', 'goodbye', 'missing', 'choice', 'happening', 'chief', 'wedding', 'strange', 'general', 'pain', 'kidding', 'decided', 'ya', 'pass', 'tired', 'class', 'officer', 'kept', 'wake', 'worse', 'busy', 'eh', 'mistake', 'kiss', 'court', 'finish', 'during', 'age', 'ship', 'caught', 'marry', 'meant', 'sell', 'dark', 'watching', 'system', 'suppose', 'evidence', 'movie', 'ride', 'completely', 'totally', 'birthday', 'tv', 'forgive', 'born', 'imagine', 'information', 'instead', 'definitely', 'security', 'certainly', 'film', 'month', 'lying', 'unless', 'train', 'seven', 'wear', 'clothes', 'michael', 'hotel', 'christmas', 'attack', 'hasn', 'round', 'expect', 'sing', 'terrible', 'george', 'history', 'blue', 'broke', 'station', 'seriously', 'forever', 'david', 'frank', 'except', 'thinks', 'message', 'entire', 'joe', 'table', 'talked', 'across', 'lovely', 'handle', 'middle', 'buddy', 'paid', 'protect', 'using', 'ran', 'swear', 'situation', 'ring', 'anywhere', 'bill', 'york', 'army', 'lead', 'bought', 'finished', 'fair', 'letter', 'attention', 'club', 'simple', 'interesting', 'space', 'test', 'box', 'group', 'single', 'sitting', 'marriage', 'join', 'fear', 'peace', 'forgot', 'force', 'normal', 'charlie', 'enjoy', 'mike', 'crime', 'ground', 'american', 'count', 'area', 'charge', 'honor', 'lunch', 'miles', 'radio', 'idiot', 'ball', 'surprise', 'paper', 'key', 'boat', 'quickly', 'gold', 'bar', 'mark', 'tom', 'wearing', 'crying', 'accident', 'government', 'eight', 'fell', 'cover', 'certain', 'interested', 'problems', 'detective', 'prison', 'major', 'stick', 'offer', 'difficult', 'smart', 'personal', 'record', 'stopped', 'hide', 'whether', 'bank', 'trip', 'america', 'public', 'list', 'afternoon', 'brain', 'fix', 'bastard', 'tea', 'service', 'screaming', 'forward', 'angry', 'park', 'soul', 'fighting', 'peter', 'agent', 'blow', 'paul', 'dress', 'mary', 'missed', 'scene', 'killing', 'standing', 'saved', 'mm', 'respect', 'killer', 'mess', 'tough', 'feels', 'church', 'cell', 'drunk', 'camera', 'mm-hmm', 'within', 'card', 'fly', 'ben', 'girlfriend', 'laugh', 'smell', 'broken', 'mum', 'honest', 'starting', 'calls', 'spent', 'third', 'english', 'visit', 'mama', 'judge', 'window', 'hungry', 'dare', 'relationship', 'moved', 'private', 'seat', 'i-i', 'position', 'lieutenant', 'realize', 'lt', 'especially', 'machine', 'walking', 'art', 'pleasure', 'bloody', 'college', 'french', 'involved', 'cry', 'became', 'lived', 'impossible', 'obviously', 'neither', 'accept', 'boyfriend', 'besides', 'queen', 'teacher', 'cops', 'sake', 'loves', 'carry', 'teach', 'apartment', 'upset', 'green', 'la', 'liked', 'cute', 'professor', 'contact', 'joke', 'cop', 'huge', 'holy', 'store', 'jail', 'likes', 'lawyer', 'doubt', 'appreciate', 'shop', 'driving', 'congratulations', 'wrote', 'village', 'field', 'james', 'wine', 'decision', 'south', 'sleeping', 'laughter', 'island', 'beginning', 'cash', 'dying', 'hundred', 'whose', 'difference', 'plane', 'push', 'continues', 'mmm', 'singing', 'eating', 'north', 'mrs', 'madam', 'gift', 'truck', 'putting', 'board', 'grab', 'beer', 'stuck', 'magic', 'support', 'rules', 'grunts', 'partner', 'reach', 'colonel', 'max', 'immediately', 'seconds', 'thousand', 'gives', 'cheers', 'victim', 'upon', 'computer', 'christ', 'planet', 'promised', 'bus', 'henry', 'search', 'staying', 'dreams', 'arrest', 'holding', 'suddenly', 'usually', 'lots', 'shoes', 'er', 'jump', 'rid', 'yo', 'knock', 'owe', 'harry', 'grow', 'worst', 'aunt', 'patient', 'kitchen', 'aah', 'fat', 'passed', 'final', 'summer', 'bob', 
'listening', 'escape', 'everywhere', 'arms', 'turns', 'address', 'ow', 'gasps', 'grand', 'yep', 'shh', 'nervous', 'de', 'choose', 'themselves', 'mate', 'drinking', 'press', 'foot', 'hadn', 'blame', 'crap', 'drugs', 'type', 'rings', 'mission', 'named', 'heaven', 'picked', 'paris', 'race', 'risk', 'books', 'further', 'danny', 'action', 'allowed', 'orders', 'learned', 'price', 'arrived', 'nick', 'otherwise', 'pictures', 'fit', 'smoke', 'favor', 'played', 'notice', 'awesome', 'smile', 'director', 'guard', 'begin', 'spot', 'surprised', 'innocent', 'narrator', 'herself', 'london', 'enemy', 'battle', 'ourselves', 'alex', 'dollars', 'allow', 'nine', 'gay', 'department', 'guilty', 'apart', 'earlier', 'duty', 'jim', 'suit', 'bell', 'west', 'legs', 'hero', 'destroy', 'stage', 'bunch', 'according', 'bigger', 'grunting', 'low', 'helping', 'admit', 'closed', 'names', 'witness', 'upstairs', 'steal', 'jimmy', 'kick', 'twice', 'cross', 'ways', 'sergeant', 'indeed', 'gas', 'keeping', 'energy', 'pregnant', 'helped', 'fired', 'favorite', 'tony', 'locked', 'places', 'writing', 'adam', 'brothers', 'starts', 'prince', 'form', 'sold', 'silly', 'mention', 'build', 'hole', 'figured', 'track', 'ringing', 'lock', 'above', 'hiding', 'steve', 'seemed', 'breakfast', 'engine', 'written', 'complete', 'video', 'applause', 'however', 'pressure', 'fresh', 'weapon', 'ms.', 'stole', 'study', 'burn', 'reading', 'crowd', 'treat', 'roll', 'double', 'spirit', 'danger', 'cost', 'empty', 'level', 'memory', 'itself', 'acting', 'interest', 'plans', 'following', 'bathroom', 'built', 'closer', 'ray', 'sarah', 'band', 'groans', 'apparently', 'excited', 'richard', 'losing', 'animals', 'flight', 'nature', 'raise', 'pop', 
'client', 'bomb', 'suspect', 'extra', 'bottle', 'van', 'mommy', 'dogs', 'wild', 'ridiculous', 'simply', 'lee', 'animal', 'showed', 'billy', 'shooting', 'keeps', 'camp', 'guns', 'medical', 'shame', 'hoping', 'whom', 'majesty', 'flowers', 'famous', 'asleep', 'beauty', 'driver', 'keys', 'awful', 'large', 'local', 'deserve', 'goddamn', 'stone', 'jane', 'grace', 'consider', 'weekend', 'wondering', 'lay', 'plenty', 'willing', 'pants', 'sweetheart', 'excellent', 'asshole', 'faith', 'beg', 'fuckin', 'responsible', 'military', 'cheering', 'opportunity', 'common', 'bottom', 'german', 'whoever', 'walked', 'papers', 'justice', 'commander', 'drug', 'main', 'knife', 'devil', 'necessary', 'although', 'princess', 'lights', 'flying', 'dick', 'rose', 'knowing', 'clearly', 
'hat', 'agreed', 'johnny', 'corner', 'code', 'note', 'tommy', 'due', 'correct', 'language', 'stars', 'faster', 'cars', 'folks', 'bullshit', 'i.', 'fellow', 'several', 'grandma', 'shows', 'leader', 'leaves', 'restaurant', 'east', 'shouting', 'blind', 'ghost', 'gotten', 'tight', 'conversation', 'tells', 'lies', 'nor', 'pulled', 'hanging', 'speed', 'stories', 'health', 'advice', 'held', 'uh-huh', 'murdered', 'beyond', 'rule', 'hardly', 'possibly', 'inspector', 'cousin', 'trial', 'emergency', 'ought', 'eddie', 'somehow', 'hearing', 'states', 'account', 'spoke', 'file', 'understood', 'angel', 
'tape', 'powerful', 'weapons', 'practice', 'manager', 'pardon', 'vote', 'jake', 'national', 'career', 'minister', 'super', 'taught', 'robert', 'biggest', 'plays', 'natural', 'dancing', 'copy', 'plus', 'martin', 'cake', 'freedom', 'among', 'breath', 'operation', 'chris', 'crew', 'challenge', 'market', 'meat', 'towards', 'bringing', 'dropped', 'student', 'lied', 'strength', 'size', 'breathe', 'color', 'monster', 'photo', 'aw', 'nearly', 'sight', 'greatest', 'games', 'bridge', 'dressed', 'arrested', 'horrible', 'planning', 'checked', 'breaking', 'noticed', 'fantastic', 'screams', 'ideas', 'investigation', 'center', 'older', 'pack', 'soldiers', 'nonsense', 'doc', 'project', 'training', 'example', 'trick', 'prepared', 'science', 'united', 'travel', 'incredible', 'grandpa', 'paying', 'character', 'teeth', 'criminal', 'charles', 'chinese', 'truly', 'honestly', 'bro', 'survive', 'bobby', 'target', 'feed', 'nurse', 'fake', 'records', 'breathing', 'sweetie', 'numbers', 'suicide', 'whoo', 'perfectly', 'amy', 'forgotten', 'remain', 'original', 'papa', 'onto', 'concerned', 'credit', 'ugh', 'invited', 
'discuss', 'research', 'easier', 'view', 'hurts', 'strike', 'roger', 'fill', 'condition', 'dr', 'nowhere', 'sheriff', 'kim', 'turning', 'brown', 'heads', 'audience', 'jealous', 'pretend', 'society', 'finding', 'shirt', 'comfortable', 'meaning', 'pieces', 
'letting', 'began', 'aye', 'jeff', 'female', 'release', 'ho', 'cards', 'pray', 'unfortunately', 'balls', 'destroyed', 'ended', 'universe', 'prepare', 'opinion', 'movies', 'soldier', 'wash', 'program', 'heat', 'usual', 'ticket', 'stolen', 'prefer', 'aware', 'surely', 'male', 'base', 'matters', 'lift', 'lab', 'command', 'proof', 'cream', 'selling', 'believed', 'create', 'afford', 'sunday', 'total', 'dumb', 'threw', 'france', 'birth', 'created', 'realized', 'british', 'noise', 'nuts', 'students', 'birds', 'social', 'brilliant', 'bodies', 'tie', 'opened', 'ours', 'bucks', 'kevin', 'mister', 'ryan', 'focus', 'dan', 'opens', 'followed', 'england', 'draw', 'purpose', 'letters', 
'daniel', 'opening', 'bullet', 'anna', 'lately', 'stayed', 'falling', 'season', 'ends', 'suggest', 'joy', 'distance', 'responsibility', 'whenever', 'issue', 'thousands', 
'process', 'sword', 'shower', 'fucked', 'lonely', 'happiness', 'eric', 'tiny', 'desk', 'pool', 'property', 'forced', 'settle', 'indistinct', 'weight', 'received', 'gang', 'bite', 'friday', 'disappeared', 'interview', 'expecting', 'kinda', 'surgery', 'horses', 'mayor', 'babe', 'ancient', 'handsome', 'thomas', 'saturday', 'lines', 'unit', 'fan', 'gentleman', 'introduce', 'fate', 'split', 'recently', 'expected', 'add', 'ordered', 'slowly', 'alarm', 'member', 'slept', 'signed', 'enter', 'spanish', 'garden', 'brings', 'brave', 'pig', 'model', 'medicine', 'access', 'failed', 'flat', 'easily', 'discovered', 'based', 'screw', 'insane', 'cares', 'weather', 'fingers', 'san', 'scott', 'path', 'harm', 'style', 'community', 'sees', 'basically', 'al', 'signal', 'nope', 'spare', 'speech', 'covered', 'shake', 'loose', 'russian', 'lake', 'ohh', 'sending', 'paint', 'remind', 'pal', 'naked', 'post', 'heading', 'streets', 'damage', 'silence', 'doors', 'pete', 'ed', 'nah', 'amount', 'members', 'kate', 'manage', 'safety', 'returned', 'harder', 'fbi', 'block', 'showing', 'fancy', 'chef', 'contract', 'dig', 'good-bye', 'drinks', 'dave', 'buried', 'brian', 'trade', 'journey', 'stomach', 'changes', 'details', 'thoughts', 'divorce', 'funeral', 'maria', 'football', 'reality', 'theory', 'gosh', 'ruined', 'gate', 'william', 'spread', 'outta', 'japanese', 'sudden', 'coat', 'sooner', 'larry', 'spring', 'page', 'ears', 'simon', 'castle', 'hidden', 'storm', 'cos', 'personally', 'artist', 'hill', 'exciting', 'permission', 'jerry', 'tickets', 'forest', 'barely', 'goin', 'regret', 'lesson', 'lover', 'andy', 'subject', 'legal', 'growing', 'ill', 'jason', 'mood', 'owner', 'caused', 'beeping', 'points', 'dating', 'loss', 'secretary', 'revenge', 'santa', 'likely', 'rent', 'connection', 'assistant', 'reasons', 'yelling', 'painting', 'trees', 'doctors', 'rush', 'foreign', 'rough', 'murderer', 'century', 'nights', 'pair', 'runs', 'farm', 'matt', 'bike', 'obvious', 
'ate', 'grew', 'professional', 'tim', 'goodness', 'parts', 'alan', 'university', 'square', 'grandfather', 'europe', 'genius', 'cases', 'ruin', 'winter', 'memories', 'da', 'buying', 'cancer', 'clock', 'dna', 'liar', 'thief', 'bleep', 'lisa', 'rights', 'including', 'competition', 'smith', 'planned', 'emily', 'boring', 'victims', 'mentioned', 'bones', 'plant', 'bless', 'warning', 'knocking', 're', 'crash', 'lower', 'silver', 'groaning', 'madame', 'defense', 'results', 'toilet', 'event', 'complicated', 'shape', 'priest', 'royal', 'romantic', 'downstairs', 'invite', 'fortune', 'tears', 'avoid', 'reached', 'higher', 'familiar', 'telephone', 'burning', 'filled', 'kelly', 'alice', 'airport', 'jobs', 'walter', 'rachel', 'giant', 'insurance', 'woods', 'scare', 'pleased', 'period', 'political', 'player', 'stops', 'secrets', 'laura', 'repeat', 'photos', 'finds', 'statement', 'suck', 'younger', 'china', 'humans', 'delicious', 'particular', 'proper', 'rome', 'belongs', 'attacked', 'bath', 'hired', 'site', 'knowledge', 
'led', 'guests', 'celebrate', 'map', 'horn', 'eventually', 'pity', 'powers', 'ashamed', 'assume', 'glasses', 'rise', 'fixed', 'request', 'officers', 'pounds', 'data', 'carefully', 'per', 'depends', 'jury', 'waited', 'positive', 'attorney', 'direction', 'families', 'doin', 'forces', 'location', 'walls', 'useless', 'grant', 'saving', 'speaks', 'fought', 'deliver', 'answers', 'changing', 'temple', 'scary', 'millions', 'offered', 'regular', 'carrying', 'official', 'jacket', 'switch', 'grave', 'chase', 'role', 'odd', 'sexy', 'faces', 'becomes', 'closes', 'badly', 'confused', 'affair', 'television', 'shock', 'raised', 'panting', 'image', 'clears', 'golden', 'patients', 'watched', 'committed', 'sexual', 'suffer', 'arthur', 'wherever', 'appear', 'chocolate', 'clever', 'hm', 'mercy', 'shots', 'lucy', 'dealing', 'trap', 'charges', 'phil', 'bang', 'poison', 'butt', 'drove', 'yourselves', 'headed', 'babies', 'yellow', 'mystery', 'picking', 'sat', 'wound', 'traffic', 'courage', 'hunt', 'indian', 'rat', 'terms', 'italian', 'emma', 'checking', 'disease', 'managed', 'winner', 'council', 'appointment', 'monday', 'crack', 'threat', 'jenny', 'physical', 'nation', 'source', 'chose', 'healthy', 'carl', 'victory', 'rick', 'stood', 'kicked', 'annie', 'disgusting', 'palace', 'below', 'shopping', 'neighborhood', 'march', 'midnight', 'piss', 'advantage', 'pure', 'india', 'aside', 'jerk', 'mail', 'effect', 'spell', 'freak', 'wood', 'screwed', 'enemies', 'gary', 'awake', 'chuckling', 'vacation', 'violence', 'leo', 'grandmother', 'modern', 'luke', 'firm', 'prime', 'heh', 'touched', 'talent', 'whore', 'piano', 'license', 'cooking', 'honour', 'concern', 'moves', 'available', 'factory', 'gods', 'value', 'central', 'union', 'studio', 'media', 'taxi', 'dies', 'iron', 'hearts', 'desire', 'rob', 'claire', 'fred', 'songs', 'washington', 'monkey', 'pride', 'pills', 'miracle', 'burned', 'smells', 'joking', 'christian', 'bleeding', 'hook', 'beating', 'protection', 'treatment', 'carter', 'metal', 'disappear', 'grateful', 'extremely', 'treasure', 'rescue', 'capable', 'passing', 'chatter', 'result', 'suffering', 'sisters', 'laid', 'governor', 'guards', 'louis', 'text', 'literally', 'remove', 'becoming', 'performance', 'stronger', 'rate', 'deeply', 'scream', 'desert', 'vehicle', 'illegal', 'pulling', 'throwing', 'josh', 'unbelievable', 'ted', 'zero', 'dean', 'curious', 'sean', 'candy', 'tied', 'edge', 'load', 'susan', 'ahh', 'mountains', 'boom', 'former', 'holiday', 'riding', 'scoffs', 'hundreds', 'motherfucker', 'sue', 'bags', 'stealing', 'appears', 'arrive', 'remains', 'decent', 'issues', 'tip', 'bride', 'penny', 'claim', 'friendship', 'desperate', 'dramatic', 'refuse', 'solve', 'theme', 'loving', 'properly', 'dragon', 'mostly', 'chuck', 'directly', 'surface', 'false', 'cast', 'junior', 'hunting', 'silent', 'thou', 'egg', 'germany', 'punch', 'africa', 'woke', 'intelligence', 'borrow', 'winning', 'falls', 'popular', 'escaped', 'witch', 'convinced', 'warn', 'announcer', 'champagne', 'kyle', 'someday', 'fallen', 'stranger', 'presence', 'tear', 'st.', 'internet', 'monsieur', 'therefore', 'technology', 'tires', 'toast', 'wise', 'clark', 'americans', 'notes', 'smoking', 'hank', 'ls', 'april', 'precious', 'rooms', 'coast', 'treated', 'material', 'released', 'uniform', 'hated', 'considered', 'exchange', 
'steps', 'blake', 'convince', 'beast', 'files', 'signs', 'drag', 'cab', 'hung', 'carried', 'ordinary', 'successful', 'eve', 'mistakes', 'houses', 'chattering', 'brains', 
'japan', 'creature', 'fourth', 'cleaning', 'california', 'lf', 'll', 'shift', 'elizabeth', 'chicago', 'exact', 'karen', 'goal', 'expert', 'served', 'direct', 'score', 'row', 'marks', 'twenty', 'series', 'section', 'pilot', 'jackson', 'darkness', 'thy', 'sale', 'destiny', 'cure', 'spoken', 'armed', 'helen', 'grade', 'tower', 'solution', 'schedule', 'explosion', 'wheel', 'cigarette', 'julie', 'fruit', 'blew', 'victor', 'talks', 'sacrifice', 'range', 'button', 'reports', 'prisoner', 'pie', 'effort', 'youth', 'eaten', 'taylor', 'knees', 'garage', 'parking', 'ambulance', 'staring', 'chances', 
'circumstances', 'sin', 'gordon', 'progress', 'unusual', 'county', 'campaign', 'vision', 'reporter', 'equipment', 'moments', 'joey', 'mass', 'alien', 'trapped', 'helps', 
'defend', 'trace', 'nasty', 'tests', 'magazine', 'rocks', 'dump', 'searching', 'connected', 'amen', 'pushed', 'merry', 'zone', 'senior', 'closing', 'freeze', 'emperor', 'incident', 'snake', 'mexico', 'lily', 'actor', 'newspaper', 'sentence', 'greg', 'leading', 'friendly', 'jones', 'chosen', 'engaged', 'julia', 'charming', 'mustn', 'anger', 'spending', 'learning', 'spy', 'sharp', 'shadow', 'warrant', 'elevator', 'kingdom', 'ricky', 'jamie', 'squad', 'wave', 'amanda', 'highness', 'kinds', 'fishing', 'sometime', 'attitude', 'sucks', 'negative', 'screen', 'workers', 'bored', 'cameras', 'similar', 'understanding', 'beeps', 'chain', 'bull', 'gasping', 'fully', 'robin', 'collect', 'morgan', 'passion', 'writer', 'empire', 'international', 'curse', 'hire', 'bastards', 'puts', 'leads', 'id', 'blows', 'sons', 'estate', 'customers', 'maggie', 'gunshot', 'i-', 'device', 'troops', 'hug', 'design', 'movement', 'thunder', 'object', 'loser', 'pen', 'sobbing', 'politics', 'despite', 'alcohol', 'climb', 'clients', 'conference', 'provide', 'marty', 'seek', 'witnesses', 'earn', 'trash', 'valley', 'fashion', 'howard', 'episode', 'prize', 'previously', 'sports', 'wanting', 'debt', 'wishes', 'hitler', 'wire', 'thee', 'circle', 'approach', 'stock', 'facts', 'remembered', 'percent', 'normally', 'tail', 'joined', 'education', 'bravo', 'library', 'rape', 'wings', 'growling', 'thrown', 'tank', 'exhales', 'authority', 'current', 'failure', 'nightmare', 'hitting', 'glory', 'knocked', 'studying', 'barry', 'agency', 'border', 'rope', 'duck', 'reputation', 'confidence', 'yard', 'beloved', 'lack', 'actual', 'skills', 'films', 'mental', 'flesh', 'anne', 'secure', 'highly', 'federal', 'sand', 'emotional', 'setting', 'nothin', 'senator', 'services', 'robbery', 'hates', 'fed', 'reward', 'theater', 'johnson', 'commit', 'patrick', 'entirely', 'extraordinary', 'ships', 'opposite', 'parties', 'stands', 'terry', 'chat', 'events', 'mummy', 'bay', 'slip', 'disappointed', 'settled', 'begins', 'andrew', 'alert', 'detail', 'pink', 'fellas', 'accepted', 
'background', 'garbage', 'panic', 'minds', 'belt', 'blowing', 'hollywood', 'agreement', 'jackie', 'pushing', 'ability', 'tiger', 'whispering', 'culture', 'saint', 'jesse', 'task', 'solid', 'doll', 'intend', 'district', 'pa', 'gee', 'custody', 'ignore', 'naturally', 'useful', 'attempt', 'abandoned', 'cutting', 'kissed', 'guarantee', 'barking', 'gather', 'policy', 'u.s.', 'violent', 'maid', 'embarrassing', 'childhood', 'wasting', 'bow', 'chick', 'sara', 'disaster', 'revolution', 'online', 'demon', 'heavily', 'coincidence', 'perform', 'thin', 'terrific', 'mac', 'crown', 'identity', 'virgin', 'impressive', 'windows', 'no-one', 'potential', 'guitar', 'committee', 'dozen', 'advance', 'quietly', 'stan', 'teaching', 'hunter', 'latest', 'hurting', 'swing', 'capital', 'counting', 'drew', 'dirt', 'whistle', 'marie', 'hits', 'doug', 'deny', 'urgent', 'threatened', 'behavior', 'molly', 'mixed', 'stays', 'assure', 'subtitles', 'explanation', 'wins', 'unique', 'chasing', 'billion', 'duke', 'production', 'slave', 'agents', 'carol', 'lets', 'cruel', 'mask', 'sally', 'behave', 'bury', 'massive', 'pathetic', 'species', 'approaching', 'jo', 'loan', 'struggle', 'trusted', 'jumped', 'firing', 
'channel', 'abby', 'stopping', 'asks', 'jean', 'swimming', 'linda', 'quarter', 'erm', 'bound', 'navy', 'article', 'accused', 'transfer', 'guts', 'quality', 'fella', 'roman', 'greater', 'damned', 'couch', 'cheer', 'vegas', 'shoe', 'title', 'shy', 'punishment', 'los', 'clicks', 'closet', 'bye-bye', 'fever', 'coward', 'flash', 'impressed', 'bruce', 'siren', 'prisoners', 'sides', 'katie', 'supply', 'sensitive', 'hopefully', 'rolling', 'roy', 'dollar', 'tone', 'voices', 'cheating', 'confess', 'demand', 'museum', 'unknown', 'drama', 'suspicious', 'adult', 'todd', 'frightened', 'warned', 'steady', 'kills', 'crossed', 'lou', 'particularly', 'laws', 'joint', 'bullets', 'package', 
'trained', 'thursday', 'boots', 'possibility', 'albert', 'civil', 'june', 'germans', 
'baseball', 'express', 'miserable', 'tuesday', 'parker', 'lion', 'joseph', 'refused', 'shine', 'assault', 'hong', 'jokes', 'breaks', 'argue', 'you-', 'trail', 'option', 'recall', 'mighty', 'collection', 'oliver', 'wilson', 'accent', 'believes', 'decisions', 'embarrassed', 'mobile', 'customer', 'terribly', 'sec', 'charity', 'considering', 
'pussy', 'donna', 'protecting', 'flag', 'kidnapped', 'italy', 'balance', 'creatures', 'nuclear', 'wallet', 'shout', 'vincent', 'entered', 'impression', 'angela', 'jay', 'degrees', 'favour', 'reaction', 'network', 'jessica', 'version', 'concert', 'gear', 'singer', 'diamond', 'defeat', 'steven', 'lane', 'blast', 'wounded', 'anytime', 'partners', 'ages', 'charlotte', 'ceremony', 'league', 'bars', 'orange', 'specific', 'conditions', 'plastic', 'crisis', 'fifth', 'term', 'self', 'offering', 'bud', 'suffered', 
'reported', 'commissioner', 'rip', 'mysterious', 'entrance', 'messed', 'tunnel', 'designed', 'neighbor', 'aboard', 'sweat', 'justin', 'ghosts', 'crimes', 'costs', 'deserves', 'dreaming', 'bust', 'el', 'teddy', 'kong', 'messages', 'enjoying', 'afterwards', 'comfort', 'mason', 'surrender', 'gym', 'kitty', 'yup', 'arranged', 'suits', 'pee', 
'stress', 'cave', 'wing', 'jordan', 'arrange', 'comrade', 'noble', 'tricks', 'betty', 'launch', 'legend', 'golf', 'imagination', 'kissing', 'tax', 'edward', 'texas', 'insist', 'marcus', 'classic', 'selfish', 'skull', 'frankie', 'shown', 'bat', 'survived', 'print', 'champion', 'bills', 'therapy', 'lifetime', 'throughout', 'a.m.', 'nathan', 'toward', 'sauce', 'experiment', 'margaret', 'describe', 'ross', 'cheat', 'attend', 
'homework', 'lewis', 'betrayed', 'servant', 'tyler', 'bible', 'practically', 'catherine', 'steel', 'wipe', 'burns', 'generation', 'cabin', 'financial', 'industry', 'bond', 'scientists', 'beaten', 'heck', 'deck', 'fans', 'script', 'brand', 'degree', 'painful', 'coughing', 'religion', 'cats', 'stephen', 'influence', 'fuel', 'drawing', 'uh-oh', 'rabbit', 'exercise', 'attractive', 'touching', 'virus', 'realise', 'torture', 'blessed', 'plain', 'rebecca', 'recent', 'barbara', 'footsteps', 'sacred', 'removed', 'pretending', 'wasted', 'jewish', 'goodnight', 'robot', 'crystal', 'confirm', 'lad', 'mile', 'division', 'scratch', 'reminds', 'walks', 'ending', 'russia', 'contest', 'valuable', 'distant', 'dumped', 'motion', 'electricity', 'centre', 'murders', 'tina', 'jeremy', 'seal', 'standard', 'ellen', 'wore', 'surrounded', 'struck', 'inform', 'gentle', 'status', 'purse', 'prints', 'players', 'charged', 'begging', 'delivered', 'kenny', 'buck', 'nina', 'construction', 'confirmed', 'confession', 'trigger', 'cells', 'frankly', 'ali', 'exit', 'response', 'cancel', 'argument', 'principal', 'turkey', 'lucas', 'clinic', 'greetings', 'neighbors', 'vice', 'toy', 'hannah', 'everyday', 'generous', 'gain', 'idiots', 'holly', 'enjoyed', 'jungle', 'link', 'underground', 'smiling', 'mistress', 'teams', 'product', 'whispers', 'religious', 'presents', 'identify', 'chip', 'chffffff', 'surveillance', 'carlos', 'vampire', 'uses', 'michelle', 'underneath', 'systems', 'temperature', 'waves', 'tribe', 'brad', 'deputy', 'sophie', 'headquarters', 'equal', 'phones', 'ken', 'reckon', 'related', 'incredibly', 'chill', 'spit', 'tracks', 'oscar', 'makeup', 'bug', 'sounded', 'spirits', 'nerve', 'divorced', 'stake', 'port', 'doorbell', 'worries', 'nephew', 'miller', 'units', 'just-', 'proceed', 'landing', 'traitor', 'outfit', 'chloe', 'bail', 'fields', 'patience', 'recording', 'foolish', 'loaded', 'tokyo', 'davis', 'costume', 'wayne', 'injured', 'somethin', 'ian', 
'pet', 'cage', 'digging', 'spain', 'seats', 'awkward', 'cleaned', 'pattern', 'filthy', 'visiting', 'jews', 'answering', 'concentrate', 'someplace', 'citizens', 'aim', 'nancy', 'affairs', 'thick', 'sport', 'basic', 'electric', 'pleasant', 'cliff', 'nail', 
'russell', 'western', 'average', 'ease', 'raped', 'interrupt', 'judy', 'satisfied', 'beep', 'starving', 'documents', 'anniversary', 'beth', 'election', 'warrior', 'forth', 'fetch', 'banks', 'placed', 'timing', 'stones', 'complex', 'frozen', 'replace', 'prayer', 'skip', 'angeles', 'guilt', 'tune', 'woo', 'actions', 'conscience', 'officially', 'martha', 'machines', 'smaller', 'determined', 'blown', 'hail', 'unhappy', 'booth', 'pour', 'berlin', 'cleared', 'packed', 'wrap', 'randy', 'behalf', 'reasonable', 'trunk', 'homes', 'festival', 'tradition', 'cigarettes', 'le', 'beside', 'harvey', 'motive', 'beings', 'bishop', 'dealer', 'defendant', 'backup', 'wounds', 'ouch', 'ann', 'nearby', 'drank', 'effects', 'jonathan', 'dennis', 'benefit', 'adventure', 'territory', 've', 'apology', 'dylan', 'unlike', 'owns', 'boxes', 'thus', 'clay', 'developed', 
'busted', 'pipe', 'gray', 'no.', 'goods', 'favourite', 'loyal', 'atmosphere', 'eva', 
'freaking', 'dropping', 'strangers', 'mouse', 'downtown', 'francisco', 'heroes', 'pit', 'rotten', 'paradise', 'meantime', 'jess', 'organization', 'hills', 'exam', 'cock', 'fairy', 'earl', 'comment', 'activity', 'frame', 'knight', 'testing', 'habit', 'shelter', 'flow', 'jennifer', 'holes', 'prevent', 'anthony', 'lend', 'cooper', 'figures', 'boston', 'sample', 'strip', 'landed', 'buzzing', 'monk', 'slightly', 'produce', 'annoying', 'judgment', 'laundry', 'ron', 'lousy', 'souls', 'existence', 'belly', 'tries', 'foster', 'returning', 'answered', 'ward', 'plants', 'actress', 'chairman', 'individual', 'hopes', 'tattoo', 'fence', 'sink', 'punk', 'confident', 'yay', 'mistaken', 'limit', 'bothering', 'st', 'uncomfortable', 'wednesday', 'gifts', 'policeman', 'na', 
'precisely', 'lawyers', 'greek', 'merely', 'criminals', 'underwear', 'hoped', 'earned', 'reveal', 'appeared', 'derek', 'heavens', 'personality', 'batman', 'virginia', 'wives', 'colour', 'worker', 'pope', 'instructions', 'intelligent', 'worrying', 'vince', 'comin', 'cried', 'traveling', 'bells', 'impact', 'robbed', 'relief', 'host', 'footage', 'odds', 'patrol', 'circus', 'mud', 'captured', 'lessons', 'occasion', 'sets', 'pulse', 'ad', 'invented', 'diamonds', 'matthew', 'auntie', 'francis', 'angels', 'hers', 'classes', 'mm-hm', 'signature', 'complain', 'blah', 'monitor', 'options', 'claims', 'flies', 'pat', 'britain', 'hid', 'wailing', 'listened', 'countries', 'vic', 'yell', 'rats', 'wondered', 'smooth', 'resist', 'companies', 'fantasy', 'passport', 'pitch', 'hammer', 'homicide', 'casey', 'holds', 'flew', 'jacob', 'noon', 'helicopter', 'dishes', 'spin', 'charm', 'slap', 'apply', 'fools', 'screeching', 'discover', 'previous', 'kit', 'authorities', 'moaning', 'photograph', 'sales', 'fifty', 'mickey', 'beneath', 'farewell', 'clouds', 'slipped', 'represent', 'deaf', 'facing', 'offense', 'citizen', 'clown', 'snap', 'messing', 'hood', 'twelve', 'interests', 'cheated', 'liz', 'informed', 'humanity', 'producer', 'technically', 'accounts', 'extreme', 'gettin', 'cia', 'ii', 'pays', 'profile', 'oxygen', 'jeez', 'gene', 'shed', 'minor', 'ex', 'theatre', 'scientific', 'lovers', 'chaos', 'l.a.', 'rocket', 'math', 'stubborn', 'august', 'oi', 'chips', 'intense', 'grey', 'talkin', 'terrorist', 'angle', 'invitation', 'gus', 
'gambling', 'respond', 'thirty', 'procedure', 'absolute', 'investigate', 'tragedy', 'stable', 'session', 'capture', 'marrying', 'ripped', 'attacks', 'stretch', 'dates', 'unable', 'gates', 'mars', 'artists', 'increase', 'tastes', 'cared', 'bottles', 'highest', 'whirring', 'meanwhile', 'nate', 'grabbed', 'pigs', 'olivia', 'wheels', 'shocked', 'reverend', 'commercial', 'escort', 'engagement', 'corpse', 'louise', 'worthy', 'scale', 'beats', 'williams', 'threatening', 'exists', 'academy', 'acts', 'hop', 'judges', 'shared', 'ralph', 'consequences', 'engineer', 'schools', 'softly', 'bombs', 'caroline', 'shark', 'transport', 'population', 'succeed', 'creepy', 'sneak', 'studies', 
'destruction', 'keith', 'protected', 'monsters', 'joining', 'punished', 'lightning', 
'malcolm', 'shell', 'fascinating', 'chamber', 'ethan', 'romance', 'instance', 'jumping', 'groups', 'exhausted', 'testify', 'studied', 'walker', 'pin', 'imagined', 'drill', 'investigating', 'ye', 'experienced', 'elena', 'necklace', 'loyalty', 'junk', 'cole', 'cries', 'stanley', 'rita', 'southern', 'blocks', 'emotions', 'begun', 'maya', 'liver', 'serving', 'matches', 'surgeon', 'granted', 'jazz', 'july', 'supplies', 'deeper', 'typical', 'kicking', 'obey', 'dancer', 'remote', 'daughters', 'moron', 'latin', 'teachers', 'toby', 'sandy', 'dragged', 'strategy', 'parent', 'jin', 'album', 'compared', 'rubbish', 'helpful', 'powder', 'sync', 'bum', 'passes', 'joan', 'choices', 'alley', 'supper', 'penis', 'alibi', 'sammy', 'pole', 'coke', 'scientist', 'fighter', 'highway', 'blade', 'alpha', 'diet', 'liquor', 'jet', 'widow', 'liberty', 'philip', 'moral', 'carrie', 'award', 'grief', 'thirsty', 'ashley', 'random', 'suspects', 'intention', 'julian', 'tools', 'driven', 'trauma', 'headache', 'safely', 'alexander', 'lads', 
'novel', 'conversations', 'waters', 'lookin', 'invisible', 'internal', 'peaceful', 'humming', 'washed', 'drives', 'talented', 'li', 'aid', 'elephant', 'troubles', 'core', 'serial', 'painted', 'divine', 'jam', 'goat', 'opera', 'thieves', 'guessing', 'objection', 'whiskey', 'florida', 'resistance', 'dressing', 'attached', 'aaron', 'brief', 
'punish', 'eternal', 'lois', 'required', 'victoria', 'fabulous', 'twins', 'characters', 'cooked', 'ln', 'ruth', 'dreamed', 'arts', 'naughty', 'stabbed', 'tend', 'diane', 
'tap', 'soap', 'locker', 'development', 'images', 'prick', 'global', 'string', 'bitter', 'sharing', 'corn', 'craig', 'fits', 'forms', 'votes', 'harold', 'propose', 'monica', 'constantly', 'granny', 'nicely', 'nerves', 'arguing', 'abuse', 'relatives', 'survival', 'gloves', 'tracking', 'zoe', 'bend', 'review', 'connect', 'separated', 'elder', 'beard', 'admiral', 'diana', 'salary', 'areas', 'disturb', 'pro', 'maintain', 'solved', 'wealth', 'bitches', 'possession', 'sang', 'gimme', 'plates', 'shoulders', 'burnt', 'recorded', 'upper', 'counts', 'tale', 'profit', 'colleague', 'warehouse', 'hostage', 'shore', 'porn', 'miami', 'fifteen', 'visitors', 'bo', 'net', 'insult', 'owen', 'cities', 'causing', 'lemon', 'heal', 'banging', 'honeymoon', 'appeal', 'marshall', 
'critical', 'creating', 'scotland', 'crane', 'enormous', 'testimony', 'praise', 'fights', 'indians', 'commission', 'growls', 'nicole', 'sins', 'fraud', 'branch', 'happily', 'bout', 'covering', 'occurred', 'raw', 'muscle', 'pages', 'tense', 'relationships', 'management', 'assignment', 'blonde', 'catching', 'exposed', 'canada', 'dont', 'han', 'von', 'comedy', 'marco', 'stroke', 'whistling', 'buildings', 'shaking', 'p.m.', 'facility', 'appropriate', 'remarkable', 'transferred', 'drawn', 'tits', 'clicking', 'symbol', 'motor', 'employees', 'ambassador', 'mothers', 'pile', 'feeding', 'soda', 'checks', 'bears', 'cookies', 'slut', 'awfully', 'stepped', 'toys', 'levels', 'differently', 'magnificent', 'steak', 'tube', 'leaders', 'superior', 'herr', 'expression', 'currently', 'throne', 'deadly', 'depressed', 'potatoes', 'wicked', 'resources', 'native', 'centuries', 'karl', 'poetry', 'multiple', 'cable', 'shortly', 'buzz', 'socks', 'fingerprints', 'goddess', 'anxious', 'september', 'colors', 'basketball', 'promises', 'explained', 'appearance', 'musical', 'sends', 'slide', 'aii', 'shawn', 'ultimate', 
'pork', 'communication', 'payment', 'structure', 'paperwork', 'obsessed', 'lazy', 'russians', 'actors', 'squeeze', 'magical', 'colleagues', 'admire', 'madness', 'roads', 
'entry', 'injury', 'burden', 'racing', 'manner', 'bits', 'norman', 'mount', 'pound', 
'visited', 'motel', 'rumbling', 'cinema', 'fond', 'halfway', 'rifle', 'reception', 'statue', 'fridge', 'brick', 'abandon', 'lap', 'natalie', 'wars', 'recommend', 'brush', 'nelson', 'pill', 'concept', 'delay', 'quarters', 'korea', 'janet', 'rub', 'mall', 'soil', 'complaint', 'sail', 'baker', 'coughs', 'bucket', 'description', 'badge', 'measure', 'hip', 'function', 'indistinctly', 'harris', 'foundation', 'labor', 'willie', 
'waiter', 'homeless', 'proved', 'unfortunate', 'log', 'meetings', 'giggles', 'combat', 'poem', 'polish', 'handed', 'mia', 'weed', 'raymond', 'tons', 'satellite', 'jersey', 'eagle', 'privacy', 'chapter', 'treating', 'wisdom', 'flip', 'entering', 'barn', 'farmer', 'clan', 'budget', 'pub', 'temporary', 'effective', 'sonny', 'wendy', 'juan', 
'plot', 'riley', 'proposal', 'sticks', 'searched', 'blessing', 'rage', 'bothered', 'sydney', 'basis', 'manners', 'recover', 'twist', 'neil', 'leak', 'item', 'catholic', 'sighing', 'retired', 'kings', 'inner', 'cents', 'affect', 'forbidden', 'patch', 'drops', 'necessarily', 'provided', 'meters', 'booked', 'returns', 'gloria', 'fires', 'humor', 'torn', 'e-mail', 'rocky', 'introduced', 'creative', 'betray', 'soviet', 'various', 'added', 'cowboy', 'suspected', 'suggested', 'delighted', 'sticking', 'shane', 'radar', 'prosecutor', 'amber', 'vast', 'quinn', 'owned', 'cookie', 'finest', 'felix', 
'pump', 'valentine', 'counter', 'sorts', 'coin', 'warren', 'slaves', 'marine', 'illness', 'sack', 'bid', 'require', 'moscow', 'largest', 'washing', 'achieve', 'causes', 'mo', 'dope', 'palm', 'logan', 'constant', 'b.', 'boo', 'medication', 'gravity', 'booze', 'noah', 'evan', 'abroad', 'christine', 'rising', 'analysis', 'cuts', 'eats', 'employee', 'vodka', 'damaged', 'solar', 'height', 'pops', 'yards', 'terrified', 'suitcase', 'chemical', 'preparing', 'advanced', 'fund', 'wears', 'chirping', 'web', 'phase', 'prom', 'suggesting', 'fleet', 'lame', 'irish', 'editor', 'october', 'assumed', 'whip', 'mel', 'region', 'amongst', 'temper', 'discussion', 'engines', 'operate', 'sunshine', 'acted', 'undercover', 'horror', 'tested', 'contrary', 'roses', 'poker', 'wrapped', 'korean', 'graham', 'mi', 'fu', 'ivan', 'focused', 'liam', 'tragic', 'carla', 'demons', 'rounds', 'entertainment', 'gathered', 'uhh', 'yells', 'lincoln', 'crossing', 
'blanket', 'nut', 'travis', 'pockets', 'limited', 'paintings', 'sober', 'caesar', 'sis', 'intended', 'niece', 'computers', 'tennis', 'needle', 'chicks', 'traditional', 'delicate', 'independent', 'leslie', 'lauren', 'grandson', 'repair', 'a.', 'brandon', 'executive', 'colin', 'recognized', 'holmes', 'regarding', 'weakness', 'aliens', 'gunshots', 'european', 'method', 'tool', 'demands', 'permit', 'towel', 'daisy', 'nowadays', 'northern', 'rangers', 'zoo', 'praying', 'antonio', 'passengers', 'con', 'australia', 'technique', 'cellphone', 'gently', 'operations', 'planes', 'bunny', 'gunfire', 'shining', 'backwards', 'skill', 'uh-', 'baron', 'kidnapping', 'iike', 'marshal', 'petty', 'sealed', 'massage', 'raising', 'menu', 'fucker', 'wagon', 'audition', 'mitch', 
'mexican', 'casino', 'bacon', 'diego', 'dutch', 'promotion', 'click', 'forgiveness', 
'burst', 'permanent', 'interfere', 'chanting', 'dammit', 'spencer', 'recovered', 'registered', 'packing', 'scenes', 'superman', 'questioning', 'unfair', 'admitted', 'ancestors', 'completed', 'conduct', 'prayers', 'sheet', 'fried', 'avenue', 'poisoned', 'reverse', 'newspapers', 'ford', 'complaining', 'senses', 'investment', 'absurd', 'potato', 'understands', 'grows', 'inspired', 'ruby', 'celebrating', 'tag', 'ram', 'requires', 'bonnie', 'bugs', 'leonard', 'elliot', 'hooked', 'jill', 'ranch', 'safer', 'worn', 'crashing', 'lands', 'heather', 'ash', 'leather', 'grounds', 'assuming', 'dana', 'conspiracy', 'thanksgiving', 'pierre', 'guardian', 'rumors', 'yen', 'megan', 'ashes', 'terror', 'misunderstanding', 'boats', 'parade', 'halt', 'immunity', 'adults', 'steam', 'kang', 'closely', 'pearl', 'soccer', 'adrian', 'priority', 'shouts', 'donald', 'happier', 'khan', 'struggling', 'root', 'larger', 'november', 'boot', 'conflict', 'laughed', 'debbie', 'cherry', 'honking', 'concerns', 'celebration', 'sore', 'unconscious', 'cattle', 'breasts', 'fairly', 'fee', 'recognise', 'wade', 'radiation', 'holidays', 'raining', 'forgetting', 'lungs', 'register', 'shadows', 'specifically', 'sarge', 
'ideal', 'turtle', 'spoil', 'deserved', 'ronnie', 'gina', 'candidate', 'lance', 'types', 'bloke', 'explode', 'immediate', 'belonged', 'identified', 'di', 'hunger', 'closest', 'combination', 'nanny', 'seth', 'gabriel', 'develop', 'detectives', 'severe', 'en', 'organized', 'franklin', 'gut', 'splendid', 'dismissed', 'pm', 'yang', 'halloween', 'ellie', 'vulnerable', 'continued', 'vital', 'comrades', 'bureau', 'drawer', 'harper', 'retreat', 'carson', 'benny', 'pillow', 'troy', 'ace', 'cart', 'nap', 'chan', 'ham', 'announce', 'borrowed', 'parked', 'galaxy', 'voted', 'muffled', 'sebastian', 'mmm-hmm', 'jewelry', 'kisses', 'luggage', 'groom', 'oops', 'lighter', 'masters', 'alliance', 'buddies', 'clothing', 'denied', 'drown', 'alike', 'excellency', 'relative', 'photographs', 'dough', 'alicia', 'wreck', 'approve', 'produced', 'christina', 'physically', 'stations', 'eli', 'samantha', 'spiritual', 'sire', 'roaring', 'stab', 'inch', 
'servants', 'limits', 'unexpected', 'arrival', 'whimpering', 'basket', 'sheets', 'scandal', 'stink', 'homer', 'tara', 'christopher', 'toes', 'shield', 'shooter', 'instant', 'objects', 'rehearsal', 'disturbing', 'directed', 'scan', 'electronic', 'republic', 'overnight', 'counsel', 'sirens', 'dorothy', 'bait', 'dignity', 'explains', 'lean', 'heroin', 'tracy', 'rex', 'barney', 'gossip', 'humble', 'economy', 'worlds', 'impress', 'clara', 'tissue', 'threaten', 'et', 'bump', 'supreme', 'bingo', 'mitchell', 'excitement', 'mankind', 'document', 'broad', 'vietnam', 'vessel', 'lit', 'dale', 'killers', 'connor', 'mario', 'foul', 'deaths', 'hut', 'elements', 'coma', 'laying', 'coffin', 'paula', 'cocaine', 'puppy', 'louder', 'handled', 'announcement', 'oath', 'mob', 'cotton', 'deposit', 'taxes', 'injuries', 'jen', 'autopsy', 'advise', 'gig', 'lecture', 'posted', 'skinny', 'lo', 'include', 'revealed', 'infected', 'relieved', 'assistance', 'solo', 'determine', 'terrorists', 'elsewhere', 'practical', 'marked', 'adorable', 'rubber', 'purple', 'operating', 'suite', 'apologies', 'personnel', 'beam', 'poet', 'samples', 'arrow', 'counselor', 'allen', 'audrey', 'spotted', 'floating', 'corrected', 'located', 'journalist', 'insisted', 'operator', 'rely', 'singh', 'fooled', 'arrives', 'i.d.', 'leon', 'walt', 'eastern', 'ay', 'shave', 'remaining', 'toss', 'anderson', 'lip', 'acid', 'nora', 'si', 'december', 'anonymous', 'inn', 'planted', 'oldest', 'breast', 'sixth', 'error', 'reporting', 'egypt', 'islands', 'brother-in-law', 'jules', 'roommate', 'sings', 'scum', 'visitor', 'giggling', 'described', 'geez', 'inches', 'commitment', 'hercules', 'react', 'cows', 'protest', 'misery', 'theft', 'embrace', 'darn', 'harsh', 'andrea', 'communicate', 'fathers', 'faithful', 'hector', 'uh-uh', 
'flame', 'medal', 'silk', 'photographer', 'trevor', 'cemetery', 'rear', 'freddy', 'banana', 'allison', 'emotion', 'chap', 'dated', 'excuses', 'shitty', 'bin', 'jew', 'gum', 'crushed', 'efforts', 'content', 'corporal', 'realised', 'del', 'rap', 'hopeless', 'debate', 'era', 'luckily', 'ton', 'liquid', 'swell', 'peggy', 'feast', 'murphy', 'attracted', 'application', 'profession', 'bench', 'vanessa', 'ahem', 'symptoms', 'scout', 'crashed', 'keen', 'aircraft', 'formed', 'hon', 'aggressive', 'pale', 'significant', 'duncan', 'clubs', 'visual', 'embassy', 'defence', 'cabinet', 'display', 'fame', 
'gibbs', 'drowned', 'wolves', 'filming', 'dunno', 'cursed', 'twin', 'sorrow', 'vault', 'defeated', 'watson', 'quote', 'penalty', 'bargain', 'speaker', 'compare', 'satan', 'helmet', 'scar', 'copies', 'fuss', 'envelope', 'perry', 'stinks', 'african', 'arrangements', 'wished', 'honored', 'believing', 'discussed', 'assigned', 'rosa', 'jenna', 'attacking', 'tin', 'sonic', 'collar', 'mere', 'romeo', 'belief', 'storage', 'rusty', 'psycho', 'climbing', 'melissa', 'fears', 'sum', 'dedicated', 'ladder', 'alternative', 'raid', 'dining', 'ms', 'corporate', 'folk', 'jon', 'replaced', 'bailey', 'un', 'heels', 'duties', 'smarter', 'existed', 'surprising', 'chess', 'requested', 'cruise', 'primary', 'rhythm', 'drum', 'models', 'motorcycle', 'adopted', 'barrel', 'cargo', 'planets', 'shove', 'wha', 'surprises', 'rosie', 'dings', 'trailer', 'cannon', 'tables', 'arse', 'ally', 'lawrence', 'wee', 'tapes', 'dull', 'sandra', 'teenage', 'kent', 'cooperate', 'risks', 'dug', 'worthless', 'arriving', 'kindness', 'ties', 'items', 'and-', 'grip', 'relations', 'rumor', 'skirt', 'frog', 'paige', 'lloyd', 'claimed', 'perfume', 'instrumental', 'flames', 'association', 'loses', 'january', 'spike', 'israel', 'eleven', 'gallery', 'ginger', 'activities', 'iraq', 'boarding', 'fist', 'stuffed', 'improve', 'creation', 'connie', 'infection', 'strikes', 'wiped', 'tension', 'whistles', 'kindly', 'certificate', 'curtis', 'bold', 'threats', 'claudia', 'sid', 'twisted', 'suspended', 'affected', 'envy', 'whale', 'dial', 'cameron', 'martial', 'controlled', 'lung', 'nigga', 'coal', 'upside', 'imperial', 'pam', 'paranoid', 'signing', 'congress', 'villa', 'candles', 'filling', 'becky', 'comic', 'faint', 'recovery', 'volunteer', 'tech', 'bleed', 'positions', 'cindy', 'forbid', 'stuart', 'perspective', 'faced', 'neat', 'pierce', 'observe', 'cycle', 'psychic', 'handling', 'goose', 'accidentally', 'conclusion', 'designer', 'sits', 'importance', 'spots', 'francs', 'sweep', 'destroying', 'communist', 'blackmail', 'pacific', 'risky', 'glorious', 'filed', 'hatred', 'cam', 'deals', 'pos', 'fooling', 'persons', 'scotch', 'executed', 'brakes', 'blank', 'tender', 'kurt', 'turner', 'tub', 'sucker', 'slight', 'addition', 'campus']


learned_words = learned.read_words()
# print(list(learned_words.keys()))

# print(len(list5k))

# clean_list = []
# common=[]
# count = 0
# for word_ in list5k:
#     if word_ not in list(learned_words.keys()) and word_.capitalize() not in list(learned_words.keys()):
#         clean_list.append(word_)
#         count+=1
#     else:
#         common.append(word_)


count2 = 0
for i in list5k:
    count2+=1
    if count2>=1000 and count2<1250:
        print(i, " -")

# print(learned_words.keys())
"""nervous  -
calm -
choose  -
choice -
myself - 
himself - 
herself - 
themselves  -
mate  -
press  -
release -
blame  -
drugs  -
ring  -
earing - 
necklece -
mission  -
named  -
heaven  -
race  -
risk  -
further  -
action  -
nickname  -
fit  -
smoke  -
favor  -
notice  -
awesome  -
smile  -
director  -
guard  -
begin  -
spot  -
surprised  -
innocent  -
enemy  -
battle  -
dollars  -
allow  -
gay  -
department  -
guilty  -
apart  -
earlier  -
duty  -
suit  -
bell  -
hero  -
destroy  -
stage  -
bunch  -
according  -
bigger  -
admit  -
witness  -
upstairs  -
steal  -
kick  -
once or twice -
cross  -
ways  -
sergeant  -
indeed  -
gas  -
energy  -
pregnant  -
to fire -
favorite  -
places  -
prince  or princess -
form  -
silly  -
mention  -
build  -
hole  -
to figure  -
to track  -
to ring-
above  -
to hide-
engine  -
to complete  -
however  -
fresh  -
weapon  -
study  -
burn  -
crowd  -
to treat  -
to roll  -
spirit  -
danger  -
cost  -
empty  -
level  -
memory  -
itself  -
acting  -
interest  -
plans  -
following  -
bathroom  -
built  -
closer  -
ray  -
band  -
apparently  -
excited  -
flight  -
nature  -
raise  -
pop  -
client  -
bomb  -
suspect  -
extra  -
bottle  -
van  -
mommy  -
dogs  -
wild  -
ridiculous  -
simply  -
animal  -
camp  -
medical  -
shame  -
hoping  -
majesty  -
flowers  -
famous  -
asleep  -
beauty  -
driver  -
keys  -
awful  -
large  -
local  -
deserve  -
goddamn  -
stone  -
jane  -
grace  -
consider  -
weekend  -
wondering  -
lay down  -
plenty  -
pants  -
sweetheart  -
excellent  -
faith  -
to beg  -
responsible  -
military  -
to cheer -
opportunity  -
common  -
bottom  -
german  -
whoever  -
walked  -
papers  -
justice  -
commander  -
drug  -
main  -
knife  -
devil  -
necessary  -
although  -
princess  -
lights  -
flying  -
rose  -
clearly  -
hat  -
agreed  -
corner  -
code  -
note  -
due  -
correct  -"""
