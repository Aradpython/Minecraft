from ursina.prefabs.first_person_controller import FirstPersonController
from turtle import textinput
from ursina import *
import random

app = Ursina()
grass_texture = load_texture('assets/grass_block.png')
stone_texture = load_texture('assets/stone_block.png')
brick_texture = load_texture('assets/brick_block.png')
dirt_texture = load_texture('assets/dirt_block.png')
block_texture  = load_texture('assets/daimond_block.png')
lava_texture = load_texture('assets/lava.png')
cheese_texture = load_texture('assets/cheese.png')
command_block_texture = load_texture('assets/command_block.png')
banana_texture = load_texture('assets/banana_block.png')
lucky_block_texture = load_texture('assets/lucky_block.png')
creeper_head_texture = load_texture('assets/creeper_head.png')
mrbeast_texture = load_texture('assets/mrbeast.png')
youtube_texture = load_texture('assets/youtube.png')
arad_texture = load_texture('assets/arad.png')
arash_texture = load_texture('assets/arash.png')
hadi_texture = load_texture('assets/hadi.png')

sky_texture = load_texture('assets/skybox_with_rocket.png')
arm_texture = load_texture('assets/arm_texture.png')

punch_sound = Audio('assets/punch_sound', loop = False, autoplay = False)
block_pick = 1

textures = [arad_texture, arash_texture, hadi_texture, youtube_texture, mrbeast_texture, stone_texture, creeper_head_texture, cheese_texture, block_texture, banana_texture, lucky_block_texture, lava_texture, command_block_texture, grass_texture, dirt_texture]

window.fps_counter.enabled = False
window.exit_button.visible = False 

def delete_all_blocks():
	for block in blocks:
		destroy(block)

def spawn_house():
	delete_all_blocks()
	for y in range(-5, 0):
		for x in range(20):
			for z in range(20):
				voxel = Voxel(x, 1, z)
				voxel = Voxel(x, y, z)
				

def update():
	global block_pick

	if held_keys['r']:
		player.gravity = -1

	if not held_keys['r']:
		player.gravity = 1

	# if held_keys['t']:
	# 	player.gravity = 0

	# if not held_keys['t']:
	# 	player.gravity = 1

	if held_keys['left mouse'] or held_keys['right mouse']:
		hand.active()

	else:
		hand.passive()

	if held_keys['1']: block_pick = 1

	if held_keys['2']: block_pick = 2

	if held_keys['3']: block_pick = 3

	if held_keys['4']: block_pick = 4

	if held_keys['5']: block_pick = 5

	if held_keys['6']: block_pick = 6

	if held_keys['7']: block_pick = 7

	if held_keys['8']: block_pick = 8

	if held_keys['9']: block_pick = 9

	if held_keys['0']: block_pick = 0

	if held_keys['`']: block_pick = 10

	if held_keys['-']: block_pick = 11

	if held_keys['=']: block_pick = 12

	if held_keys['q']: block_pick = -1

	if held_keys['*']: block_pick = 13

	if held_keys['/']: block_pick = 14

	if held_keys['+']: block_pick = 15

class Voxel(Button):
	def __init__(self, position : tuple = (0,0,0), texture = grass_texture, *args):
		super().__init__(
			parent = scene,
			position = position,
			model = 'assets/block',
			origin_y = 0.5,
			texture = texture,
			color = color.color(0, 0, random.uniform(0.9, 1)),
			scale = 0.5)
			

	def input(self, key):
		if self.hovered:
			if key == 'left mouse down':
				# punch_sound.play()
				if block_pick == -1: pass
				if block_pick == 1: voxel = Voxel(position = self.position + mouse.normal, texture = grass_texture)
				if block_pick == 2: voxel = Voxel(position = self.position + mouse.normal, texture = stone_texture)
				if block_pick == 3: voxel = Voxel(position = self.position + mouse.normal, texture = brick_texture)
				if block_pick == 4: voxel = Voxel(position = self.position + mouse.normal, texture = dirt_texture)
				if block_pick == 5: voxel = Voxel(position = self.position + mouse.normal, texture = block_texture)
				if block_pick == 6: voxel = Voxel(position = self.position + mouse.normal, texture = lava_texture)
				if block_pick == 7: voxel = Voxel(position = self.position + mouse.normal, texture = cheese_texture)
				if block_pick == 8: voxel = Voxel(position = self.position + mouse.normal, texture = command_block_texture)
				if block_pick == 9: voxel = Voxel(position = self.position + mouse.normal, texture = banana_texture)
				if block_pick == 0: voxel = Voxel(position = self.position + mouse.normal, texture = lucky_block_texture)
				if block_pick == 10: voxel = Voxel(position = self.position + mouse.normal, texture = creeper_head_texture)
				if block_pick == 11: voxel = Voxel(position = self.position + mouse.normal, texture = mrbeast_texture)
				if block_pick == 12: voxel = Voxel(position = self.position + mouse.normal, texture = youtube_texture)
				if block_pick == 13: voxel = Voxel(position = self.position + mouse.normal, texture = arad_texture)
				if block_pick == 14: voxel = Voxel(position = self.position + mouse.normal, texture = arash_texture)
				if block_pick == 15: voxel = Voxel(position = self.position + mouse.normal, texture = hadi_texture)

			if key == 'right mouse down':
				# punch_sound.play()
				destroy(self)

class Sky(Entity):
	def __init__(self):
		super().__init__(
			parent = scene,
			model = 'sphere',
			texture = sky_texture,
			scale = 250,
			double_sided = True)

class Hand(Entity):
	def __init__(self):
		super().__init__(
			parent = camera.ui,
			model = 'assets/arm',
			texture = arm_texture,
			scale = 0.2,
			rotation = Vec3(150,-10,0),
			position = Vec2(0.4,-0.6))
		

	def active(self):
		self.position = Vec2(0.3,-0.5)

	def passive(self):
		self.position = Vec2(0.4,-0.6)

player = FirstPersonController()
sky = Sky()
hand = Hand()

blocks = []



for y in range(-10, -5):
	for z in range(20):
		for x in range(20):
			voxel = Voxel(position=(x, y, z), texture=grass_texture)

for y in range(-5, 1):
	for z in range(5, 5):
		for x in range(5, 5):
			voxel = Voxel(position=(x, y, z), texture=random.choice(textures))
			# blocks.append(voxel)

# spawn_house()



app.run()