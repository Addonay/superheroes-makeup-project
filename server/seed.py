from flask import Flask
import random
from models import db, Hero, Power,HeroPower

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'  # Update with your database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db.init_app(app)

# Create and populate the database with seed data
with app.app_context():
    db.create_all()

    # Create Heroes
    heroes_data = [
        Hero(name='Kamala Khan', supername='Ms. Marvel', image_url="https://i.pinimg.com/originals/06/9e/fe/069efee45779e514f1ff75e0474a6b13.jpg"),
        Hero(name='Doreen Green', supername='Squirrel Girl', image_url="https://i.pinimg.com/originals/20/51/2e/20512e95f3a2b46c3e89f205f1a5b053.jpg"),
        Hero(name='Gwen Stacy', supername='Spider-Gwen', image_url="https://i.pinimg.com/originals/03/32/c1/0332c184fd2b3cd55141dec33fe77f9c.jpg"),
        Hero(name='Clark Kent', supername='Superman', image_url="https://i.pinimg.com/originals/d5/a4/58/d5a4583eec522e14592e0508d21fce36.jpg"),
        Hero(name='Bruce Wayne', supername='Batman', image_url="https://i.pinimg.com/originals/24/34/85/243485fa289d5b6b85e15d3e3d6bd734.jpg"),
        Hero(name='Diana Prince', supername='Wonder Woman', image_url="https://i.pinimg.com/originals/06/e8/10/06e81024faeca13fb353d79802105ff3.jpg"),
        Hero(name='Barry Allen', supername='The Flash', image_url="https://i.pinimg.com/originals/35/9a/59/359a5966e6e446faac5128dfcfed72d1.jpg"),
        Hero(name='Arthur Curry', supername='Aquaman', image_url="https://i.pinimg.com/originals/b0/57/6d/b0576d0a4ea73c033a8bee0389bc0aa0.jpg"),
        Hero(name='Hal Jordan', supername='Green Lantern', image_url="https://i.pinimg.com/originals/6d/36/8c/6d368c6a2762670f4ed0da62cc585d9c.png"),
        Hero(name='Tony Stark', supername='Iron Man', image_url="https://i.pinimg.com/originals/71/2a/3a/712a3a78794e59820bbfdbbd8290cb24.jpg"),
        Hero(name='Steve Rogers', supername='Captain America', image_url="https://i.pinimg.com/originals/47/7b/87/477b879603756ef9fe04f4eaff912d54.jpg"),
        Hero(name='Natasha Romanoff', supername='Black Widow', image_url="https://i.pinimg.com/originals/57/81/cb/5781cbbafd26407fd3cd162d46749a2e.jpg"),
        Hero(name='Thor Odinson', supername='Thor', image_url="https://i.pinimg.com/originals/52/99/55/52995502d4cb6e6d39b128b2ab9f240f.jpg"),
        Hero(name='Peter Parker', supername='Spider-Man', image_url="https://i.pinimg.com/originals/b2/36/f5/b236f5e48098735c92f89d9668f122e7.jpg"),
        Hero(name='Wade Wilson', supername='Deadpool', image_url="https://i.pinimg.com/originals/f5/a9/0e/f5a90edaf12e7dfc7059b42a97ab6ad8.jpg"),
        Hero(name='Carol Danvers', supername='Captain Marvel', image_url="https://i.pinimg.com/originals/69/85/ff/6985ff3602be4ffff038ed633a8e6850.jpg"),
        Hero(name="King T'Challa", supername='Black Panther', image_url="https://i.pinimg.com/originals/43/6d/e2/436de27a6de7527052e42f59e925b064.jpg"),
        Hero(name="Shaun", supername='Shang-Chi', image_url="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/846a9086-8a40-43e0-aa10-2fc7d6d73730/dep1e7n-25fa3924-678b-44cf-ae3a-ed5481799c59.jpg/v1/fit/w_750,h_1126,q_70,strp/shang_chi__2021__teaser_poster_textless_by_mintmovi3_dep1e7n-375w-2x.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTkyMCIsInBhdGgiOiJcL2ZcLzg0NmE5MDg2LThhNDAtNDNlMC1hYTEwLTJmYzdkNmQ3MzczMFwvZGVwMWU3bi0yNWZhMzkyNC02NzhiLTQ0Y2YtYWUzYS1lZDU0ODE3OTljNTkuanBnIiwid2lkdGgiOiI8PTEyODAifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ._waitD9ixsH3jhF-0yBjTZBjO4nifbuTx3jFVBRvuKA"),
        Hero(name="Kara Zor-El", supername='Super Girl', image_url="https://i.pinimg.com/originals/72/8e/d3/728ed3a17e48cb7b2b14f4723dc6253b.jpg"),
        Hero(name='Scott Lang', supername='Ant-Man', image_url="https://i.pinimg.com/originals/60/2d/9b/602d9bd2ae0007d7d61a684dd766ec72.png"),
        Hero(name='Jean Grey', supername='Phoenix', image_url="https://i.pinimg.com/originals/48/fb/a7/48fba7f1ff120cb5adb5ffcf7c44b6bf.png"),
        Hero(name='Bruce Banner', supername='The Hulk', image_url="https://i.pinimg.com/originals/15/62/dd/1562dd7b35ec0a53ce105a451ea931d9.jpg"),
        Hero(name='Scott Summers', supername='Cyclops', image_url="https://i.pinimg.com/originals/19/98/55/19985548dd02f141aa68e461dd39f380.jpg"),
        Hero(name='Matt Murdock', supername='Daredevil', image_url="https://i.pinimg.com/originals/66/a5/f8/66a5f83d0de9e6248fe87d7cf6e3a931.jpg"),
        Hero(name='Steven Strange', supername='Dr Strange', image_url="https://i.pinimg.com/originals/e6/28/d0/e628d050d2f3bbd9dfdbb62e5bfd9915.jpg"),
        Hero(name='Oliver Queen', supername='Green Arrow', image_url="https://i.pinimg.com/originals/b8/79/23/b8792308f9d8975fe0e68fce4e029426.jpg"),
        Hero(name='Wanda Maximoff', supername='Scarlet Witch', image_url="https://i.pinimg.com/originals/3f/b9/e4/3fb9e468a2a12204ed24579acde1e7fd.jpg"),
        Hero(name='Victor Stone', supername='Cyborg', image_url="https://i.pinimg.com/564x/cc/f0/92/ccf0928f9149c559bb6e3c9d70f91041.jpg"),
        Hero(name='Billy Batson', supername='Shazam', image_url="https://i.pinimg.com/564x/3a/97/6f/3a976f739a4e5448a8c53fe87b531322.jpg"),
        Hero(name='Teh Adam', supername='Black Adam', image_url="https://i.pinimg.com/564x/f1/6f/27/f16f27523e3ebd2ef33b7d51204cdb2c.jpg"),
        Hero(name="J'onn J'onzz", supername="Martian Manhunter", image_url="https://i.pinimg.com/564x/95/86/c6/9586c6ad690dabad53fdfdd678b3f20a.jpg"),
        Hero(name='Selina Kyle', supername='Catwoman', image_url="https://i.pinimg.com/564x/64/bd/63/64bd63bf651d875a7168973bbb81dfa3.jpg"),
        Hero(name='Dick Greyson', supername='Nightwing', image_url="https://i.pinimg.com/564x/d0/e8/b9/d0e8b967559b2ad20f7f2022794de402.jpg"),
        Hero(name='Barbara Gordon', supername='Batgirl', image_url="https://i.pinimg.com/564x/55/dd/e7/55dde7e6ad46c830065aafc46dde4be1.jpg"),
        Hero(name='Jefferson Jackson', supername='Firestorm', image_url="https://i.pinimg.com/564x/96/67/4b/96674b006b58ace1ca2ac33dd7d3fea7.jpg"),
        Hero(name='Ororo Munroe', supername='Storm', image_url="https://i.pinimg.com/564x/97/70/22/9770226526f5f05e7cd72676b1da9c81.jpg"),
        Hero(name='Norrin Radd', supername='Silver Surfer', image_url="https://i.pinimg.com/750x/a8/b0/ae/a8b0ae6734624b73540743fdf5b644bb.jpg"),
        Hero(name='Reed Richards', supername='Mr. Fantastic', image_url="https://i.pinimg.com/564x/af/81/c9/af81c999c3d5697d572fb126138ee760.jpg"),
        Hero(name='Sue Storm', supername='Invisible Woman', image_url="https://i.pinimg.com/564x/f7/a3/6a/f7a36ab56a08f7f1726a547198c5e439.jpg"),
        Hero(name='Ben Grimm', supername='The Thing', image_url="https://i.pinimg.com/564x/c3/9a/8e/c39a8e3eaf863efd7cc01517b3efa9b5.jpg"),
        Hero(name='Johnny Storm', supername='Human Torch', image_url="https://i.pinimg.com/564x/15/4b/e9/154be9c3e924f12b5170a7bc7d230e2f.jpg"),
        Hero(name='Peter Quill', supername='Star-Lord', image_url="https://i.pinimg.com/564x/7b/62/53/7b62538a10245d0852c4fc7cce32df9c.jpg"),
        Hero(name='Zoe Saldana', supername='Gamora', image_url="https://i.pinimg.com/564x/25/b3/d3/25b3d362b7207f0c5ba8d744ba799824.jpg"),
        Hero(name='Drax', supername='Drax the Destroyer', image_url="https://i.pinimg.com/564x/16/57/62/1657626bf1073411977f9e5602cc4bc9.jpg"),
        Hero(name='Rocket', supername='Rocket Raccoon', image_url="https://i.pinimg.com/564x/d4/2b/8d/d42b8d1ff0833fa52452c0ba7a450abf.jpg"),
        Hero(name='Groot', supername='Groot', image_url="https://i.pinimg.com/564x/71/e9/ea/71e9ea8c3fb195a2c2e16a803a27bbce.jpg"),
        Hero(name='Jessica Jones', supername='Jessica Jones', image_url="https://i.pinimg.com/564x/30/cd/ef/30cdef0fb5109e213eecbddede7173e7.jpg"),
        Hero(name='Luke Cage', supername='Luke Cage', image_url="https://i.pinimg.com/564x/36/0f/d6/360fd61f49223272cb82c6832dd91877.jpg"),
        Hero(name='Danny Rand', supername='Iron Fist', image_url="https://i.pinimg.com/564x/20/84/50/20845022050d6b99ae942a6ed7f13de5.jpg"),
        Hero(name='Nick Fury', supername='Agent Nick', image_url="https://i.pinimg.com/564x/21/67/97/216797efa96509ea3157265703d48864.jpg"),
        Hero(name='Jeniffer Walters', supername='She Hulk', image_url="https://i.pinimg.com/564x/7b/3a/90/7b3a9039a572d39fa7fba271213e06ce.jpg"),
        Hero(name='Steve Grant', supername='Moon Knight', image_url="https://i.pinimg.com/564x/74/e0/71/74e071622cd944fa6fd05512e656538b.jpg"),
        Hero(name='Querl Dox', supername='Brainiac 5', image_url="https://i.pinimg.com/564x/10/5b/6e/105b6ec7a35ddb7b78dc551e960b0883.jpg"),
        Hero(name='Jackman Wolverine', supername='Wolverine', image_url="https://i.pinimg.com/564x/03/78/b4/0378b4eb082a73520fe6248d14178402.jpg"),
        Hero(name='Karen Gillian', supername='Nebula', image_url="https://i.pinimg.com/564x/4f/31/12/4f311288babccd86ae0207e8eee9597d.jpg"),
        Hero(name='Mike Rooker', supername='Yondu', image_url="https://i.pinimg.com/236x/85/38/a6/8538a65d262e5888e26b349909fdb656.jpg"),
        Hero(name='Pom Klementiff', supername='Mantis', image_url="https://i.pinimg.com/236x/d8/da/1b/d8da1ba91aec1aaf1101350cde6e0e86.jpg"),
        Hero(name='Jackman Wolverine', supername='Vision', image_url="https://i.pinimg.com/236x/12/75/4a/12754ac600a5806ac7e401e776382952.jpg"),
        Hero(name='Bucky Burners', supername='Winter Soldier', image_url="https://i.pinimg.com/236x/97/7b/2f/977b2fd1fa40c5c9e635df525edf6372.jpg"),
        Hero(name='Clint Barton', supername='Hawkeye', image_url="https://i.pinimg.com/236x/3c/9c/35/3c9c35fa657e079a2bd68f5f806f5032.jpg"),
        Hero(name='James Rhodes', supername='War Machine', image_url="https://i.pinimg.com/236x/56/eb/34/56eb34e76287027d1c7fb5e5de23ac3d.jpg"),
        Hero(name='Samuel Wilson', supername='Falcon', image_url="https://i.pinimg.com/236x/55/7c/54/557c54fe28707305e1a09eafff6d9760.jpg"),
        Hero(name='Wally West', supername='Kid Flash', image_url="https://i.pinimg.com/236x/05/2c/03/052c036b19040cedb2ebbbf0ad1c8aa0.jpg"),
        Hero(name='America Chavez', supername='Miss America', image_url="https://i.pinimg.com/564x/a2/e8/7b/a2e87be465ba74282225b9436eeb0093.jpg"),
        Hero(name='Teegan Croft', supername='Raven', image_url="https://i.pinimg.com/236x/f5/1d/b4/f51db4bdd1fa26110597a2b880239337.jpg"),
        Hero(name='Jason Todd', supername='Robin', image_url="https://i.pinimg.com/236x/ca/f5/67/caf5678da7792937cdff6820a698a5b5.jpg"),
        Hero(name='Cisco Ramon', supername='Vibe', image_url="https://i.pinimg.com/236x/83/64/78/836478481645506457cd584f88b720e5.jpg"),
        Hero(name='Caitlin Snow', supername='Killer Frost', image_url="https://i.pinimg.com/236x/ba/e8/14/bae814122e3864bd2047a5243eec323d.jpg"),
        Hero(name='Alicia Garcia', supername='Ultraviolet', image_url="https://i.pinimg.com/236x/66/bb/49/66bb49349eadd0397a7a8bda22d16abe.jpg"),
        Hero(name='Mick Rory', supername='Heat Wave', image_url="https://i.pinimg.com/236x/eb/60/2b/eb602ba8d49bfc7a68a81dbb53600f2b.jpg"),
        Hero(name='Carter Hall', supername='Hawkman', image_url="https://i.pinimg.com/236x/98/a4/9e/98a49e85ac106c020398dcfd86fc6df3.jpg"),
        Hero(name='Clifford DeVoe', supername='Thinker', image_url="https://i.pinimg.com/236x/12/af/27/12af2721d8e92904319def917a555769.jpg"),
        Hero(name='Leonard Snart', supername='Captain Cold', image_url="https://i.pinimg.com/236x/98/70/b2/9870b2230830cd63269442d5c75e80ea.jpg"),
        Hero(name='Jimmy Olsen', supername='Guardian', image_url="https://i.pinimg.com/236x/7a/ff/8e/7aff8ed9693d431b88f2550a6e1351dd.jpg"),
        Hero(name='Samanthha Arias', supername='Reign', image_url="https://i.pinimg.com/236x/ec/93/05/ec9305de09465480936be075f340c7c1.jpg"),
        Hero(name='Ben Lockwood', supername='Agent Liberty', image_url="https://i.pinimg.com/236x/93/f9/29/93f9296252b56b546a15ec232369b6cb.jpg"),
        Hero(name='Nil Nal', supername='Dreamer', image_url="https://i.pinimg.com/236x/8d/d2/86/8dd286f30c47fa5f7245119828a40044.jpg"),
        Hero(name='Andrea Rojas', supername='Acrata', image_url="https://i.pinimg.com/474x/07/e3/f5/07e3f53eccae1b55e7596b7cb9a2e288.jpg"),
        Hero(name='Mar Novu', supername='The Monitor', image_url="https://i.pinimg.com/236x/c7/ff/c7/c7ffc78467d83ccb78a3bfb494451a19.jpg"),
        Hero(name='Leslie Willis', supername='Livewire', image_url="https://i.pinimg.com/236x/3c/77/5f/3c775f49631cd65248248e9a35f2eb78.jpg"),
        Hero(name='Nyxlygsptlnz', supername='Nyxly', image_url="https://static.wikia.nocookie.net/arrow/images/3/31/Nyxlygsptlnz.png"),
        Hero(name='Mxyzptlk', supername='Myxy', image_url="https://static.wikia.nocookie.net/arrow/images/e/e0/Mxyzptlk.png"),
        Hero(name="M'gann M'orzz", supername='Miss Martian', image_url="https://i.pinimg.com/236x/c8/48/f8/c848f84b5ee9346b283a4bebb738aca0.jpg"),
        Hero(name='Siobkhan Smythe', supername='Banshee', image_url="https://i.pinimg.com/236x/51/cd/ff/51cdffc173fb0bd6fd3ea7412fd27c92.jpg"),
        Hero(name='Raymond Jensen', supername='Parasite', image_url="https://i.pinimg.com/236x/88/77/ad/8877ad6d8ae1b152c34d671c33b896b7.jpg"),
    ]

    # heroes = [Hero(**hero_data) for hero_data in heroes_data]
    db.session.add_all(heroes_data)
    db.session.commit()


    # Create Powers
    powers_data = [
        Power(name='Superhuman Strength', description='Grants the ability to lift incredibly heavy objects and deliver powerful punches.'),
        Power(name='Superhuman Durability', description="Enhances the body's resilience, making it resistant to physical harm."),
        Power(name='Flight', description='Allows the superhero to soar through the skies with great agility and speed.'),
        Power(name='Super Speed', description='Enables the superhero to move at incredible velocities.'),
        Power(name='Enhanced Agility', description='Provides exceptional balance and coordination.'),
        Power(name='Healing Factor', description='Accelerates the healing process, allowing for rapid recovery from injuries.'),
        Power(name='Enhanced Senses', description='Heightens sensory perception, including sight, hearing, and smell.'),
        Power(name='Energy Projection', description='Empowers the superhero to unleash energy-based attacks.'),
        Power(name='Telepathy', description='Enables the superhero to communicate through thoughts and read minds.'),
        Power(name='Martial Arts Expertise', description='Masters various combat styles for hand-to-hand combat.'),
        Power(name='Elasticity', description='Allows the superhero to stretch and shape-shift their body.'),
        Power(name='Squirrel Control', description='Grants the ability to communicate with and command squirrels.'),
        Power(name='Dimensional Travel', description='Enables the superhero to move between different dimensions.'),
        Power(name='Heat Vision', description='Emits powerful heat beams from the eyes.'),
        Power(name='Genius-level Intelligence', description='Possesses exceptional intelligence and problem-solving skills.'),
        Power(name='Lasso of Truth', description='Forces anyone ensnared to tell the truth.'),
        Power(name='Time Travel', description='Allows the superhero to travel through time using their speed.'),
        Power(name='Aquatic Telepathy', description='Communicates with and commands sea creatures.'),
        Power(name='Green Lantern Ring', description='Creates energy constructs using the power of the ring.'),
        Power(name='Powered Armor Suit', description='Provides flight and various weapon systems.'),
        Power(name='Vibranium Shield', description='Carries an indestructible shield.'),
        Power(name='Espionage and Martial Arts Mastery', description='Excells in espionage and martial arts.'),
        Power(name='Control over Lightning', description='Wields control over lightning with Mjolnir.'),
        Power(name='Web-shooters', description='Shoots webs for swinging and trapping foes.'),
        Power(name='Regenerative Healing', description='Heals rapidly from injuries.'),
        Power(name='Energy Absorption and Projection', description='Absorbs and projects energy.'),
        Power(name='Vibranium Suit and Enhanced Senses', description='Wears a Vibranium suit and possesses enhanced senses.'),
        Power(name='Size Manipulation', description='Can shrink or grow in size.'),
        Power(name='Telekinesis and Telepathy', description='Boasts vast psychic abilities.'),
        Power(name='Transforming into the Hulk', description='Gains super strength and durability upon transformation.')
    ]

    # powers = [Power(**power_data) for power_data in powers_data]
    db.session.add_all(powers_data)
    db.session.commit()


    # Create HeroPower associations
    heropower_assignments = [
        {'hero_id': 1, 'power_id': 1, 'strength': 'Average'},
        {'hero_id': 2, 'power_id': 2, 'strength': 'Weak'},
        {'hero_id': 3, 'power_id': 3, 'strength': 'Strong'},
        {'hero_id': 4, 'power_id': 4, 'strength': 'Average'},
        {'hero_id': 5, 'power_id': 5, 'strength': 'Weak'},
        {'hero_id': 6, 'power_id': 6, 'strength': 'Strong'},
        {'hero_id': 7, 'power_id': 7, 'strength': 'Average'},
        {'hero_id': 8, 'power_id': 8, 'strength': 'Weak'},
        {'hero_id': 9, 'power_id': 9, 'strength': 'Strong'},
        {'hero_id': 10, 'power_id': 10, 'strength': 'Average'},
        {'hero_id': 11, 'power_id': 11, 'strength': 'Weak'},
        {'hero_id': 12, 'power_id': 12, 'strength': 'Strong'},
        {'hero_id': 13, 'power_id': 13, 'strength': 'Average'},
        {'hero_id': 14, 'power_id': 14, 'strength': 'Weak'},
        {'hero_id': 15, 'power_id': 15, 'strength': 'Strong'},
        {'hero_id': 16, 'power_id': 16, 'strength': 'Average'},
        {'hero_id': 17, 'power_id': 17, 'strength': 'Weak'},
        {'hero_id': 18, 'power_id': 18, 'strength': 'Strong'},
        {'hero_id': 19, 'power_id': 19, 'strength': 'Average'},
        {'hero_id': 20, 'power_id': 20, 'strength': 'Weak'},
        {'hero_id': 21, 'power_id': 21, 'strength': 'Strong'},
        {'hero_id': 22, 'power_id': 22, 'strength': 'Average'},
        {'hero_id': 23, 'power_id': 23, 'strength': 'Weak'},
        {'hero_id': 24, 'power_id': 24, 'strength': 'Strong'},
        {'hero_id': 25, 'power_id': 25, 'strength': 'Average'},
        {'hero_id': 26, 'power_id': 26, 'strength': 'Weak'},
        {'hero_id': 27, 'power_id': 27, 'strength': 'Strong'},
        {'hero_id': 28, 'power_id': 28, 'strength': 'Average'},
        {'hero_id': 29, 'power_id': 29, 'strength': 'Weak'},
        {'hero_id': 30, 'power_id': 0, 'strength': 'Strong'},
        {'hero_id': 31, 'power_id': 1, 'strength': 'Average'},
        {'hero_id': 32, 'power_id': 2, 'strength': 'Weak'},
        {'hero_id': 33, 'power_id': 3, 'strength': 'Strong'},
        {'hero_id': 34, 'power_id': 4, 'strength': 'Average'},
        {'hero_id': 35, 'power_id': 5, 'strength': 'Weak'},
        {'hero_id': 36, 'power_id': 6, 'strength': 'Strong'},
        {'hero_id': 37, 'power_id': 7, 'strength': 'Average'},
        {'hero_id': 38, 'power_id': 8, 'strength': 'Weak'},
        {'hero_id': 39, 'power_id': 9, 'strength': 'Strong'},
        {'hero_id': 40, 'power_id': 10, 'strength': 'Average'},
        {'hero_id': 41, 'power_id': 11, 'strength': 'Weak'},
        {'hero_id': 42, 'power_id': 12, 'strength': 'Strong'},
        {'hero_id': 43, 'power_id': 13, 'strength': 'Average'},
        {'hero_id': 44, 'power_id': 14, 'strength': 'Weak'},
        {'hero_id': 45, 'power_id': 15, 'strength': 'Strong'},
        {'hero_id': 46, 'power_id': 16, 'strength': 'Average'},
        {'hero_id': 47, 'power_id': 17, 'strength': 'Weak'},
        {'hero_id': 48, 'power_id': 18, 'strength': 'Strong'},
        {'hero_id': 49, 'power_id': 19, 'strength': 'Average'},
        {'hero_id': 50, 'power_id': 20, 'strength': 'Weak'},
        {'hero_id': 51, 'power_id': 21, 'strength': 'Strong'},
        {'hero_id': 52, 'power_id': 22, 'strength': 'Average'},
        {'hero_id': 53, 'power_id': 23, 'strength': 'Weak'},
        {'hero_id': 54, 'power_id': 24, 'strength': 'Strong'},
        {'hero_id': 55, 'power_id': 25, 'strength': 'Average'},
        {'hero_id': 56, 'power_id': 26, 'strength': 'Weak'},
        {'hero_id': 57, 'power_id': 27, 'strength': 'Strong'},
        {'hero_id': 58, 'power_id': 28, 'strength': 'Average'},
        {'hero_id': 59, 'power_id': 29, 'strength': 'Weak'},
        {'hero_id': 60, 'power_id': 0, 'strength': 'Strong'},
        {'hero_id': 61, 'power_id': 1, 'strength': 'Average'},
        {'hero_id': 62, 'power_id': 2, 'strength': 'Weak'},
        {'hero_id': 63, 'power_id': 3, 'strength': 'Strong'},
        {'hero_id': 64, 'power_id': 4, 'strength': 'Average'},
        {'hero_id': 65, 'power_id': 5, 'strength': 'Weak'},
        {'hero_id': 66, 'power_id': 6, 'strength': 'Strong'},
        {'hero_id': 67, 'power_id': 7, 'strength': 'Average'},
        {'hero_id': 68, 'power_id': 8, 'strength': 'Weak'},
        {'hero_id': 69, 'power_id': 9, 'strength': 'Strong'},
        {'hero_id': 70, 'power_id': 10, 'strength': 'Average'},
        {'hero_id': 71, 'power_id': 11, 'strength': 'Weak'},
        {'hero_id': 72, 'power_id': 12, 'strength': 'Strong'},
        {'hero_id': 73, 'power_id': 13, 'strength': 'Average'},
        {'hero_id': 74, 'power_id': 14, 'strength': 'Weak'},
        {'hero_id': 75, 'power_id': 15, 'strength': 'Strong'},
        {'hero_id': 76, 'power_id': 16, 'strength': 'Average'},
        {'hero_id': 77, 'power_id': 17, 'strength': 'Weak'},
        {'hero_id': 78, 'power_id': 18, 'strength': 'Strong'},
        {'hero_id': 79, 'power_id': 19, 'strength': 'Average'},
        {'hero_id': 80, 'power_id': 20, 'strength': 'Weak'},
        {'hero_id': 81, 'power_id': 21, 'strength': 'Strong'},
        {'hero_id': 82, 'power_id': 22, 'strength': 'Average'},
        {'hero_id': 83, 'power_id': 23, 'strength': 'Weak'},
        {'hero_id': 84, 'power_id': 24, 'strength': 'Strong'},
    ]



    heropowers = []
    for assignment in heropower_assignments:
        hero = heroes_data[assignment['hero_id']]
        power = powers_data[assignment['power_id']]
        strength = assignment['strength']
        hero_powers = HeroPower(strength=strength, hero=hero, power=power)
        heropowers.append(hero_powers)

    db.session.add_all(heropowers)
    db.session.commit()

    

    print("Database seeded successfully!")