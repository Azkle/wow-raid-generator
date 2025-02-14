import random
tanks = ['Blood Death Knight', 'Brewmaster Monk', 'Guardian Druid', 'Protection Paladin', 'Protection Warrior',
'Vengeance Demonhunter']
healers = ['Discipline Priest', 'Holy Paladin', 'Holy Priest', 'Mistweaver Monk', 'Preservation Evoker',
'Restoration Druid', 'Restoration Shaman']
melee = ['Arms Warrior', 'Assassination Rogue', 'Enhancement Shaman', 'Feral Druid', 'Frost Death Knight',
'Fury Warrior', 'Havoc Demonhunter', 'Outlaw Rogue', 'Retribution Paladin', 'Subtlety Rogue', 'Survival Hunter',
'Unholy Death Knight', 'Windwalker Monk']
ranged = ['Affliction Warlock', 'Arcane Mage', 'Augmentation Evoker', 'Balance Druid', 'Beast Mastery Hunter',
'Demonology Warlock', 'Destruction Warlock', 'Devastation Evoker', 'Elemental Shaman', 'Fire Mage', 'Frost Mage',
'Marksmanship Hunter', 'Shadow Priest']
Role = [tanks, healers, melee, ranged]
raidtanks = []
raidheal = []
raidmel = []
raidrang = []
raiddps = []
raidsize = int(input('How many raiders do you have? '))
healnum = round(int(raidsize/5))
dpsnum = raidsize - healnum - 2
melnum = round(dpsnum / random.randint(1, int(dpsnum)))
rangnum = dpsnum - melnum
for i in range(2):
    list.append(raidtanks, random.choice(tanks))

for i in range(healnum):
    list.append(raidheal, random.choice(healers))

for i in range(melnum):
    list.append(raidmel, random.choice(melee))
if rangnum > 0:
    for i in ranged:
        list.append(raidrang, random.choice(ranged))
print(f"Your tanks are {' and '.join(raidtanks)}.")
print(f"Your healers are {', '.join(raidheal)}.")
raiddps.extend(raidmel)
raiddps.extend(raidrang)
print(f"Your DPS are {', '.join(raiddps)}.")