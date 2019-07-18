from django.db import models
import datetime


class homeproject(models.Model):
	title = models.CharField(max_length=500, default='', blank=True)
	title2 = models.CharField(max_length=500, default='', blank=True)
	date = models.DateField(default=datetime.date.today)

	def __str__(self):
		return self.title



class aboutus(models.Model):
	title = models.CharField(max_length=200,default='', blank=True )
	Body1 = models.TextField(default='', blank=True)
	Body2 = models.TextField(default='', blank=True)
	Body3 = models.TextField(default='', blank=True)

	def __str__(self):
		return self.title

class contactinfo(models.Model):
	
	team_name = models.CharField(max_length=100, default='', blank=True )
	name = models.CharField(max_length=50, default='' ,blank=True)
	phone_number1 = models.CharField(max_length=20, default='' ,blank=True)
	phone_number2 = models.CharField(max_length=20, default='' ,blank=True)
	phone_number3 = models.CharField(max_length=20, default='' ,blank=True)
	phone_number4 = models.CharField(max_length=20, default='' ,blank=True)
	phone_number5 = models.CharField(max_length=20, default='' ,blank=True)
	phone_number6 = models.CharField(max_length=20, default='' ,blank=True)
	phone_number7 = models.CharField(max_length=20, default='' ,blank=True)
	phone_number8 = models.CharField(max_length=20, default='' ,blank=True)
	phone_number9 = models.CharField(max_length=20, default='' ,blank=True)
	phone_number10 = models.CharField(max_length=20, default='',blank=True)


	email1 = models.EmailField(max_length=150, default='youname@something.com',blank=True)
	email2 = models.EmailField(max_length=150, default='youname@something.com', blank=True)
	email3 = models.EmailField(max_length=150, default='youname@something.com', blank=True)
	email4 = models.EmailField(max_length=150, default='youname@something.com', blank=True)
	email5 = models.EmailField(max_length=150, default='youname@something.com', blank=True)
	email6 = models.EmailField(max_length=150, default='youname@something.com',blank=True)
	email7 = models.EmailField(max_length=150, default='youname@something.com', blank=True)
	email8 = models.EmailField(max_length=150, default='youname@something.com', blank=True)
	email9 = models.EmailField(max_length=150, default='youname@something.com', blank=True)
	email10 = models.EmailField(max_length=150, default='youname@something.com', blank=True)

	def __str__(self):
		return self.team_name


# class Manufacture(models.Model):
# 	title = models.CharField(max_length=500, default='', blank=True )
# 	text = models.CharField(max_length=500, default='', blank=True ,null=True)
# 	# img1 = models.ImageField(upload_to='Project', blank=True)
# 	# img2 = models.ImageField(upload_to='Project', blank=True)
# 	# img3 = models.ImageField(upload_to='Project', blank=True)
# 	# img4 = models.ImageField(upload_to='Project', blank=True)

# 	def __str__(self):
# 		return self.title

class eventi(models.Model):
	title = models.CharField(max_length=500, default='', blank=True)
	text = models.CharField(max_length=500, default='', null=True, blank=True)
	img1 = models.ImageField(upload_to='Project', blank=True)
	img2 = models.ImageField(upload_to='Project', blank=True)
	img3 = models.ImageField(upload_to='Project', blank=True)
	img4 = models.ImageField(upload_to='Project', blank=True)
	img5 = models.ImageField(upload_to='Project', blank=True)
	img6 = models.ImageField(upload_to='Project', blank=True)
	img7 = models.ImageField(upload_to='Project', blank=True)
	img8 = models.ImageField(upload_to='Project', blank=True)
	img9 = models.ImageField(upload_to='Project', blank=True)
	title2 = models.CharField(max_length=500, default='', blank=True)
	text2 = models.CharField(max_length=500, default='', null=True, blank=True)
	img10 = models.ImageField(upload_to='Project', blank=True)
	img11 = models.ImageField(upload_to='Project', blank=True)
	img12 = models.ImageField(upload_to='Project', blank=True)
	img13 = models.ImageField(upload_to='Project', blank=True)

	def __str__(self):
		return self.title


# class ourteam(models.Model):
# 	title = models.CharField(max_length=200,default='', blank=True )
# 	Body1 = models.TextField(default='', blank=True , blank=True)
# 	Body2 = models.TextField(default='', blank=True , blank=True)
# 	Body3 = models.TextField(default='', blank=True , blank=True)

# 	def __str__(self):
# 		return self.title


# class news(models.Model):
# 	title = models.CharField(max_length=200, default='', blank=True , blank=True)
# 	text = models.CharField(max_length=5000, default='', blank=True , blank=True)
# 	infowindow = models.TextField(default='', blank=True , blank=True)
# 	img = models.ImageField(upload_to='Project', blank=True, blank=True)

# 	def __str__(self):
# 		return self.title



















class fubrication_errection_of_steel_structure(models.Model):
	title = models.CharField(max_length=500, default='', blank=True)
	text = models.CharField(max_length=500, default='', null=True, blank=True)
	img1 = models.ImageField(upload_to='Project', blank=True)
	img2 = models.ImageField(upload_to='Project', blank=True)
	img3 = models.ImageField(upload_to='Project', blank=True)
	img4 = models.ImageField(upload_to='Project', blank=True)

	def __str__(self):
		return self.title




class fabrication_and_coating(models.Model):
	title = models.CharField(max_length=500, default='', blank=True )
	text = models.CharField(max_length=500, default='', blank=True ,null=True)
	img1 = models.ImageField(upload_to='Project', blank=True)
	img2 = models.ImageField(upload_to='Project', blank=True)
	img3 = models.ImageField(upload_to='Project', blank=True)

	def __str__(self):
		return self.title
#-----------------------------------------------------------------------------------------

class Manufacture_and_maintenance(models.Model):
	title = models.CharField(max_length=500, default='', blank=True )
	text = models.CharField(max_length=500, default='', blank=True ,null=True)
	img1 = models.ImageField(upload_to='Project', blank=True)
	img2 = models.ImageField(upload_to='Project', blank=True)
	img3 = models.ImageField(upload_to='Project', blank=True)
	img4 = models.ImageField(upload_to='Project', blank=True)

	def __str__(self):
		return self.title



class Construction_and_repair(models.Model):
	title = models.CharField(max_length=500, default='', blank=True )
	text = models.CharField(max_length=500, default='', blank=True ,null=True)
	img1 = models.ImageField(upload_to='Project', blank=True)
	img2 = models.ImageField(upload_to='Project', blank=True)
	img3 = models.ImageField(upload_to='Project', blank=True)
	img4 = models.ImageField(upload_to='Project', blank=True)
	img5 = models.ImageField(upload_to='Project', blank=True)
	img6 = models.ImageField(upload_to='Project', blank=True)
	img7 = models.ImageField(upload_to='Project', blank=True)
	img8 = models.ImageField(upload_to='Project', blank=True)
	img9 = models.ImageField(upload_to='Project', blank=True)
	img10 = models.ImageField(upload_to='Project', blank=True)
	img11 = models.ImageField(upload_to='Project', blank=True)
	img12 = models.ImageField(upload_to='Project', blank=True)

	def __str__(self):
		return self.title
#-----------------------------------------------------------------------------------------

class Oil_tank_fire(models.Model):
	title = models.CharField(max_length=500, default='', blank=True )
	text = models.CharField(max_length=500, default='', blank=True ,null=True)
	img1 = models.ImageField(upload_to='Project', blank=True)
	img2 = models.ImageField(upload_to='Project', blank=True)

	def __str__(self):
		return self.title


class Piping_construction(models.Model):
	title = models.CharField(max_length=500, default='', blank=True )
	text = models.CharField(max_length=500, default='', blank=True ,null=True)
	img1 = models.ImageField(upload_to='Project', blank=True)
	img2 = models.ImageField(upload_to='Project', blank=True)
	img3 = models.ImageField(upload_to='Project', blank=True)
	img4 = models.ImageField(upload_to='Project', blank=True)
	img5 = models.ImageField(upload_to='Project', blank=True)
	img6 = models.ImageField(upload_to='Project', blank=True)
	img7 = models.ImageField(upload_to='Project', blank=True)
	img8 = models.ImageField(upload_to='Project', blank=True)

	def __str__(self):
		return self.title


class Piping_construction2(models.Model):
	title = models.CharField(max_length=500, default='', blank=True )
	text = models.CharField(max_length=500, default='', blank=True ,null=True)
	img1 = models.ImageField(upload_to='Project', blank=True)
	img2 = models.ImageField(upload_to='Project', blank=True)
	img3 = models.ImageField(upload_to='Project', blank=True)
	img4 = models.ImageField(upload_to='Project', blank=True)
	img5 = models.ImageField(upload_to='Project', blank=True)

	def __str__(self):
		return self.title
#-----------------------------------------------------------------------------------------

class Ammonia_spherical_tank_maintenance(models.Model):
	title = models.CharField(max_length=500, default='', blank=True )
	text = models.CharField(max_length=500, default='', blank=True ,null=True)
	img1 = models.ImageField(upload_to='Project', blank=True)


	def __str__(self):
		return self.title


class Copper_heat_exchanger(models.Model):
	title = models.CharField(max_length=500, default='', blank=True )
	text = models.CharField(max_length=500, default='', blank=True ,null=True)
	img1 = models.ImageField(upload_to='Project', blank=True)
	img2 = models.ImageField(upload_to='Project', blank=True)
	img3 = models.ImageField(upload_to='Project', blank=True)
	img4 = models.ImageField(upload_to='Project', blank=True)

	def __str__(self):
		return self.title


class Dismandteling_and_reconstruction(models.Model):
	title = models.CharField(max_length=500, default='', blank=True )
	text = models.CharField(max_length=500, default='', blank=True ,null=True)
	img1 = models.ImageField(upload_to='Project', blank=True)
	img2 = models.ImageField(upload_to='Project', blank=True)
	img3 = models.ImageField(upload_to='Project', blank=True)
	img4 = models.ImageField(upload_to='Project', blank=True)
	img5 = models.ImageField(upload_to='Project', blank=True)
	img6 = models.ImageField(upload_to='Project', blank=True)
	img7 = models.ImageField(upload_to='Project', blank=True)

	def __str__(self):
		return self.title


class Dismantle_a_waste_heat_boiler(models.Model):
	title = models.CharField(max_length=500, default='', blank=True )
	text = models.CharField(max_length=500, default='', blank=True ,null=True)
	img1 = models.ImageField(upload_to='Project', blank=True)
	img2 = models.ImageField(upload_to='Project', blank=True)
	img3 = models.ImageField(upload_to='Project', blank=True)

	def __str__(self):
		return self.title


class Maintenance_of_heat_exchangers(models.Model):
	title = models.CharField(max_length=500, default='', blank=True )
	text = models.CharField(max_length=500, default='', blank=True ,null=True)
	img1 = models.ImageField(upload_to='Project', blank=True)
	img2 = models.ImageField(upload_to='Project', blank=True)
	img3 = models.ImageField(upload_to='Project', blank=True)
	img4 = models.ImageField(upload_to='Project', blank=True)
	img5 = models.ImageField(upload_to='Project', blank=True)

	def __str__(self):
		return self.title


class Heat_exchanger_repair(models.Model):
	title = models.CharField(max_length=500, default='', blank=True )
	text = models.CharField(max_length=500, default='', blank=True ,null=True)
	img1 = models.ImageField(upload_to='Project', blank=True)
	img2 = models.ImageField(upload_to='Project', blank=True)
	img3 = models.ImageField(upload_to='Project', blank=True)
	img4 = models.ImageField(upload_to='Project', blank=True)
	img5 = models.ImageField(upload_to='Project', blank=True)
	img6 = models.ImageField(upload_to='Project', blank=True)
	img7 = models.ImageField(upload_to='Project', blank=True)
	img8 = models.ImageField(upload_to='Project', blank=True)
	img9 = models.ImageField(upload_to='Project', blank=True)
	img10 = models.ImageField(upload_to='Project', blank=True)
	img11 = models.ImageField(upload_to='Project', blank=True)
	img12 = models.ImageField(upload_to='Project', blank=True)
	img13 = models.ImageField(upload_to='Project', blank=True)
	img14 = models.ImageField(upload_to='Project', blank=True)
	img15 = models.ImageField(upload_to='Project', blank=True)
	img16 = models.ImageField(upload_to='Project', blank=True)
	def __str__(self):
		return self.title


class Retubing_heat_exchanger(models.Model):
	title = models.CharField(max_length=500, default='', blank=True )
	text = models.CharField(max_length=500, default='', blank=True ,null=True)
	img1 = models.ImageField(upload_to='Project', blank=True)
	img2 = models.ImageField(upload_to='Project', blank=True)
	img3 = models.ImageField(upload_to='Project', blank=True)
	img4 = models.ImageField(upload_to='Project', blank=True)

	def __str__(self):
		return self.title


class Tanks_Fabrication(models.Model):
	title = models.CharField(max_length=500, default='', blank=True )
	text = models.CharField(max_length=500, default='', blank=True ,null=True)
	img1 = models.ImageField(upload_to='Project', blank=True)
	img2 = models.ImageField(upload_to='Project', blank=True)
	img3 = models.ImageField(upload_to='Project', blank=True)
	img4 = models.ImageField(upload_to='Project', blank=True)

	def __str__(self):
		return self.title


class Titanium_tube_at_nitric_acid_plant(models.Model):
	title = models.CharField(max_length=500, default='', blank=True )
	text = models.CharField(max_length=500, default='', blank=True ,null=True)
	img1 = models.ImageField(upload_to='Project', blank=True)
	img2 = models.ImageField(upload_to='Project', blank=True)
	img3 = models.ImageField(upload_to='Project', blank=True)
	img4 = models.ImageField(upload_to='Project', blank=True)
	img5 = models.ImageField(upload_to='Project', blank=True)

	def __str__(self):
		return self.title
#-----------------------------------------------------------------------------------------

class Manufacture_of_hard_wear_core(models.Model):
	title = models.CharField(max_length=500, default='', blank=True )
	text = models.CharField(max_length=500, default='', blank=True ,null=True)
	img1 = models.ImageField(upload_to='Project', blank=True)
	img2 = models.ImageField(upload_to='Project', blank=True)
	img3 = models.ImageField(upload_to='Project', blank=True)
	img4 = models.ImageField(upload_to='Project', blank=True)
	img5 = models.ImageField(upload_to='Project', blank=True)

	def __str__(self):
		return self.title


class Selection_of_the_suitable_hard_facing_electrocle(models.Model):
	title = models.CharField(max_length=500, default='', blank=True )
	text = models.CharField(max_length=500, default='', blank=True ,null=True)
	img1 = models.ImageField(upload_to='Project', blank=True)
	img2 = models.ImageField(upload_to='Project', blank=True)
	img3 = models.ImageField(upload_to='Project', blank=True)

	def __str__(self):
		return self.title
#-----------------------------------------------------------------------------------------

class Maintenance_of_heavy_trucks_structure(models.Model):
	title = models.CharField(max_length=500, default='', blank=True )
	text = models.CharField(max_length=500, default='', blank=True ,null=True)
	img1 = models.ImageField(upload_to='Project', blank=True)
	img2 = models.ImageField(upload_to='Project', blank=True)
	img3 = models.ImageField(upload_to='Project', blank=True)
	img4 = models.ImageField(upload_to='Project', blank=True)

	def __str__(self):
		return self.title


class Manufacture_and_welding_of_heads_of_heavy_trucks(models.Model):
	title = models.CharField(max_length=500, default='', blank=True )
	text = models.CharField(max_length=500, default='', blank=True ,null=True)
	img1 = models.ImageField(upload_to='Project', blank=True)
	img2 = models.ImageField(upload_to='Project', blank=True)
	img3 = models.ImageField(upload_to='Project', blank=True)
	img4 = models.ImageField(upload_to='Project', blank=True)
	img5 = models.ImageField(upload_to='Project', blank=True)
	img6 = models.ImageField(upload_to='Project', blank=True)
	img7 = models.ImageField(upload_to='Project', blank=True)
	img8 = models.ImageField(upload_to='Project', blank=True)
	img9 = models.ImageField(upload_to='Project', blank=True)
	img10 = models.ImageField(upload_to='Project', blank=True)
	img11 = models.ImageField(upload_to='Project', blank=True)
	img12 = models.ImageField(upload_to='Project', blank=True)

	def __str__(self):
		return self.title


class Repair_of_damaged_hydrolic_pislon_of_loader(models.Model):
	title = models.CharField(max_length=500, default='', blank=True )
	text = models.CharField(max_length=500, default='', blank=True ,null=True)
	img1 = models.ImageField(upload_to='Project', blank=True)
	img2 = models.ImageField(upload_to='Project', blank=True)
	img3 = models.ImageField(upload_to='Project', blank=True)
	img4 = models.ImageField(upload_to='Project', blank=True)
	img5 = models.ImageField(upload_to='Project', blank=True)
	img6 = models.ImageField(upload_to='Project', blank=True)
	img7 = models.ImageField(upload_to='Project', blank=True)
	img8 = models.ImageField(upload_to='Project', blank=True)
	img9 = models.ImageField(upload_to='Project', blank=True)
	img10 = models.ImageField(upload_to='Project', blank=True)
	img11 = models.ImageField(upload_to='Project', blank=True)
	def __str__(self):
		return self.title




class Repair_of_treated_and_cracked_loader_bucket(models.Model):
	title = models.CharField(max_length=500, default='', blank=True )
	text = models.CharField(max_length=500, default='', blank=True ,null=True)
	img1 = models.ImageField(upload_to='Project', blank=True)
	img2 = models.ImageField(upload_to='Project', blank=True)
	img3 = models.ImageField(upload_to='Project', blank=True)
	img4 = models.ImageField(upload_to='Project', blank=True)
	img5 = models.ImageField(upload_to='Project', blank=True)
	img6 = models.ImageField(upload_to='Project', blank=True)

	def __str__(self):
		return self.title


class Welding_repair_of_heavy_truck_rims(models.Model):
	title = models.CharField(max_length=500, default='', blank=True )
	text = models.CharField(max_length=500, default='', blank=True ,null=True)
	img1 = models.ImageField(upload_to='Project', blank=True)
	img2 = models.ImageField(upload_to='Project', blank=True)
	img3 = models.ImageField(upload_to='Project', blank=True)

	def __str__(self):
		return self.title
#-----------------------------------------------------------------------------------------

class Dismanteling_old_expansion_joint(models.Model):
	title = models.CharField(max_length=500, default='', blank=True )
	text = models.CharField(max_length=500, default='', blank=True ,null=True)
	img1 = models.ImageField(upload_to='Project', blank=True)
	img2 = models.ImageField(upload_to='Project', blank=True)
	img3 = models.ImageField(upload_to='Project', blank=True)
	img4 = models.ImageField(upload_to='Project', blank=True)
	img5 = models.ImageField(upload_to='Project', blank=True)
	img6 = models.ImageField(upload_to='Project', blank=True)
	img7 = models.ImageField(upload_to='Project', blank=True)

	def __str__(self):
		return self.title


class Dismanteling_the_DRI_reactor_spod(models.Model):
	title = models.CharField(max_length=500, default='', blank=True )
	text = models.CharField(max_length=500, default='', blank=True ,null=True)
	img1 = models.ImageField(upload_to='Project', blank=True)
	img2 = models.ImageField(upload_to='Project', blank=True)
	img3 = models.ImageField(upload_to='Project', blank=True)
	img4 = models.ImageField(upload_to='Project', blank=True)
	img5 = models.ImageField(upload_to='Project', blank=True)
	img6 = models.ImageField(upload_to='Project', blank=True)
	img7 = models.ImageField(upload_to='Project', blank=True)
	img8 = models.ImageField(upload_to='Project', blank=True)
	img9 = models.ImageField(upload_to='Project', blank=True)

	def __str__(self):
		return self.title
#-----------------------------------------------------------------------------------------

class Compressor_housing_ss304_repair(models.Model):
	title = models.CharField(max_length=500, default='', blank=True )
	text = models.CharField(max_length=500, default='', blank=True ,null=True)
	img1 = models.ImageField(upload_to='Project', blank=True)
	img2 = models.ImageField(upload_to='Project', blank=True)
	img3 = models.ImageField(upload_to='Project', blank=True)
	img4 = models.ImageField(upload_to='Project', blank=True)
	img5 = models.ImageField(upload_to='Project', blank=True)
	img6 = models.ImageField(upload_to='Project', blank=True)
	img7 = models.ImageField(upload_to='Project', blank=True)
	img8 = models.ImageField(upload_to='Project', blank=True)
	img9 = models.ImageField(upload_to='Project', blank=True)
	img10 = models.ImageField(upload_to='Project', blank=True)
	def __str__(self):
		return self.title


class Replacement_of_the_second_stage_of_nitricacid_lower_ss304L(models.Model):
	title = models.CharField(max_length=500, default='', blank=True )
	text = models.CharField(max_length=500, default='', blank=True ,null=True)
	img1 = models.ImageField(upload_to='Project', blank=True)
	img2 = models.ImageField(upload_to='Project', blank=True)
	img3 = models.ImageField(upload_to='Project', blank=True)
	img4 = models.ImageField(upload_to='Project', blank=True)
	img5 = models.ImageField(upload_to='Project', blank=True)

	def __str__(self):
		return self.title


class Welding_repair_ss304H_tube_cladded_innerly(models.Model):
	title = models.CharField(max_length=500, default='', blank=True )
	text = models.CharField(max_length=500, default='', blank=True ,null=True)
	img1 = models.ImageField(upload_to='Project', blank=True)
	img2 = models.ImageField(upload_to='Project', blank=True)
	img3 = models.ImageField(upload_to='Project', blank=True)
	img4 = models.ImageField(upload_to='Project', blank=True)
	img5 = models.ImageField(upload_to='Project', blank=True)
	img6 = models.ImageField(upload_to='Project', blank=True)
	img7 = models.ImageField(upload_to='Project', blank=True)
	img8 = models.ImageField(upload_to='Project', blank=True)
	img9 = models.ImageField(upload_to='Project', blank=True)
	img10 = models.ImageField(upload_to='Project', blank=True)
	img11 = models.ImageField(upload_to='Project', blank=True)
	img12 = models.ImageField(upload_to='Project', blank=True)
	img13 = models.ImageField(upload_to='Project', blank=True)
	img14 = models.ImageField(upload_to='Project', blank=True)
	img15 = models.ImageField(upload_to='Project', blank=True)
	img16 = models.ImageField(upload_to='Project', blank=True)
	img17 = models.ImageField(upload_to='Project', blank=True)
	img18 = models.ImageField(upload_to='Project', blank=True)
	img19 = models.ImageField(upload_to='Project', blank=True)
	img20 = models.ImageField(upload_to='Project', blank=True)

	def __str__(self):
		return self.title

#-----------------------------------------------------------------------------------------
class Welding_of_Broken_and_cracked_parts_for_cast_iron_pump_housing(models.Model):
	title = models.CharField(max_length=500, default='', blank=True )
	text = models.CharField(max_length=500, default='', blank=True ,null=True)
	img1 = models.ImageField(upload_to='Project', blank=True)
	img2 = models.ImageField(upload_to='Project', blank=True)
	img3 = models.ImageField(upload_to='Project', blank=True)
	img4 = models.ImageField(upload_to='Project', blank=True)
	img5 = models.ImageField(upload_to='Project', blank=True)
	img6 = models.ImageField(upload_to='Project', blank=True)


	def __str__(self):
		return self.title


class Welding_of_Broken_and_cracked_parts_for_cast_iron_pump_housing2(models.Model):
	title = models.CharField(max_length=500, default='', blank=True )
	text = models.CharField(max_length=500, default='', blank=True ,null=True)
	img1 = models.ImageField(upload_to='Project', blank=True)
	img2 = models.ImageField(upload_to='Project', blank=True)
	img3 = models.ImageField(upload_to='Project', blank=True)
	img4 = models.ImageField(upload_to='Project', blank=True)
	img5 = models.ImageField(upload_to='Project', blank=True)
	img6 = models.ImageField(upload_to='Project', blank=True)
	img7 = models.ImageField(upload_to='Project', blank=True)
	img8 = models.ImageField(upload_to='Project', blank=True)
	img9 = models.ImageField(upload_to='Project', blank=True)
	img10 = models.ImageField(upload_to='Project', blank=True)
	img11 = models.ImageField(upload_to='Project', blank=True)
	img12 = models.ImageField(upload_to='Project', blank=True)
	img13 = models.ImageField(upload_to='Project', blank=True)
	img14 = models.ImageField(upload_to='Project', blank=True)
	img15 = models.ImageField(upload_to='Project', blank=True)
	img16 = models.ImageField(upload_to='Project', blank=True)
	img17 = models.ImageField(upload_to='Project', blank=True)
	img18 = models.ImageField(upload_to='Project', blank=True)
	img19 = models.ImageField(upload_to='Project', blank=True)
	img20 = models.ImageField(upload_to='Project', blank=True)
	img21 = models.ImageField(upload_to='Project', blank=True)
	img22 = models.ImageField(upload_to='Project', blank=True)
	img23 = models.ImageField(upload_to='Project', blank=True)
	img24 = models.ImageField(upload_to='Project', blank=True)

	def __str__(self):
		return self.title
#-----------------------------------------------------------------------------------------

class Copper_Welding_Project_1(models.Model):
	title = models.CharField(max_length=500, default='', blank=True )
	text = models.CharField(max_length=500, default='', blank=True ,null=True)
	img1 = models.ImageField(upload_to='Project', blank=True)
	img2 = models.ImageField(upload_to='Project', blank=True)
	img3 = models.ImageField(upload_to='Project', blank=True)
	img4 = models.ImageField(upload_to='Project', blank=True)

	def __str__(self):
		return self.title


class Copper_Welding_Project_2(models.Model):
	title = models.CharField(max_length=500, default='', blank=True )
	text = models.CharField(max_length=500, default='', blank=True ,null=True)
	img1 = models.ImageField(upload_to='Project', blank=True)
	img2 = models.ImageField(upload_to='Project', blank=True)
	img3 = models.ImageField(upload_to='Project', blank=True)
	img4 = models.ImageField(upload_to='Project', blank=True)

	def __str__(self):
		return self.title
#-----------------------------------------------------------------------------------------

class Aluminume_welding_project_1(models.Model):
	title = models.CharField(max_length=500, default='', blank=True )
	text = models.CharField(max_length=500, default='', blank=True ,null=True)
	img1 = models.ImageField(upload_to='Project', blank=True)
	img2 = models.ImageField(upload_to='Project', blank=True)
	img3 = models.ImageField(upload_to='Project', blank=True)
	img4 = models.ImageField(upload_to='Project', blank=True)

	def __str__(self):
		return self.title


class Aluminume_welding_project_2(models.Model):
	title = models.CharField(max_length=500, default='', blank=True )
	text = models.CharField(max_length=500, default='', blank=True ,null=True)
	img1 = models.ImageField(upload_to='Project', blank=True)
	img2 = models.ImageField(upload_to='Project', blank=True)
	img3 = models.ImageField(upload_to='Project', blank=True)
	img4 = models.ImageField(upload_to='Project', blank=True)

	def __str__(self):
		return self.title

#-----------------------------------------------------------------------------------------
class Dismanteling_and_welding_repair_of_reformer_incoloy_800_tube(models.Model):
	title = models.CharField(max_length=500, default='', blank=True )
	text = models.CharField(max_length=500, default='', blank=True ,null=True)
	img1 = models.ImageField(upload_to='Project', blank=True)
	img2 = models.ImageField(upload_to='Project', blank=True)
	img3 = models.ImageField(upload_to='Project', blank=True)
	img4 = models.ImageField(upload_to='Project', blank=True)
	img5 = models.ImageField(upload_to='Project', blank=True)
	img6 = models.ImageField(upload_to='Project', blank=True)
	img7 = models.ImageField(upload_to='Project', blank=True)
	img8 = models.ImageField(upload_to='Project', blank=True)
	img9 = models.ImageField(upload_to='Project', blank=True)

	def __str__(self):
		return self.title


class Repair_of_incolloy_800_header_of_reforme_at_amonia(models.Model):
	title = models.CharField(max_length=500, default='', blank=True )
	text = models.CharField(max_length=500, default='', blank=True ,null=True)
	img1 = models.ImageField(upload_to='Project', blank=True)
	img2 = models.ImageField(upload_to='Project', blank=True)
	img3 = models.ImageField(upload_to='Project', blank=True)
	img4 = models.ImageField(upload_to='Project', blank=True)
	img5 = models.ImageField(upload_to='Project', blank=True)
	img6 = models.ImageField(upload_to='Project', blank=True)
	img7 = models.ImageField(upload_to='Project', blank=True)
	img8 = models.ImageField(upload_to='Project', blank=True)
	img9 = models.ImageField(upload_to='Project', blank=True)

	def __str__(self):
		return self.title


#-------------------------------------------------------------------------

class Cold_welding_project1(models.Model):
	title = models.CharField(max_length=500, default='', blank=True )
	text = models.CharField(max_length=500, default='', blank=True ,null=True)
	img1 = models.ImageField(upload_to='Project', blank=True)
	img2 = models.ImageField(upload_to='Project', blank=True)
	img3 = models.ImageField(upload_to='Project', blank=True)
	img4 = models.ImageField(upload_to='Project', blank=True)

	def __str__(self):
		return self.title


class Cold_welding_project2(models.Model):
	title = models.CharField(max_length=500, default='', blank=True )
	text = models.CharField(max_length=500, default='', blank=True ,null=True)
	img1 = models.ImageField(upload_to='Project', blank=True)
	img2 = models.ImageField(upload_to='Project', blank=True)
	img3 = models.ImageField(upload_to='Project', blank=True)
	img4 = models.ImageField(upload_to='Project', blank=True)

	def __str__(self):
		return self.title


class Cold_welding_project3(models.Model):
	title = models.CharField(max_length=500, default='', blank=True )
	text = models.CharField(max_length=500, default='', blank=True ,null=True)
	img1 = models.ImageField(upload_to='Project', blank=True)
	img2 = models.ImageField(upload_to='Project', blank=True)
	img3 = models.ImageField(upload_to='Project', blank=True)
	img4 = models.ImageField(upload_to='Project', blank=True)

	def __str__(self):
		return self.title


class Cold_welding_project4(models.Model):
	title = models.CharField(max_length=500, default='', blank=True )
	text = models.CharField(max_length=500, default='', blank=True ,null=True)
	img1 = models.ImageField(upload_to='Project', blank=True)
	img2 = models.ImageField(upload_to='Project', blank=True)
	img3 = models.ImageField(upload_to='Project', blank=True)
	img4 = models.ImageField(upload_to='Project', blank=True)

	def __str__(self):
		return self.title


class Cold_welding_project5(models.Model):
	title = models.CharField(max_length=500, default='', blank=True )
	text = models.CharField(max_length=500, default='', blank=True ,null=True)
	img1 = models.ImageField(upload_to='Project', blank=True)
	img2 = models.ImageField(upload_to='Project', blank=True)
	img3 = models.ImageField(upload_to='Project', blank=True)
	img4 = models.ImageField(upload_to='Project', blank=True)

	def __str__(self):
		return self.title




class Cold_welding_project6(models.Model):
	title = models.CharField(max_length=500, default='', blank=True )
	text = models.CharField(max_length=500, default='', blank=True ,null=True)
	img1 = models.ImageField(upload_to='Project', blank=True)
	img2 = models.ImageField(upload_to='Project', blank=True)
	img3 = models.ImageField(upload_to='Project', blank=True)
	img4 = models.ImageField(upload_to='Project', blank=True)

	def __str__(self):
		return self.title


class Cold_welding_project7(models.Model):
	title = models.CharField(max_length=500, default='', blank=True )
	text = models.CharField(max_length=500, default='', blank=True ,null=True)
	img1 = models.ImageField(upload_to='Project', blank=True)
	img2 = models.ImageField(upload_to='Project', blank=True)
	img3 = models.ImageField(upload_to='Project', blank=True)
	img4 = models.ImageField(upload_to='Project', blank=True)

	def __str__(self):
		return self.title


class Cold_welding_project8(models.Model):
	title = models.CharField(max_length=500, default='', blank=True )
	text = models.CharField(max_length=500, default='', blank=True ,null=True)
	img1 = models.ImageField(upload_to='Project', blank=True)
	img2 = models.ImageField(upload_to='Project', blank=True)
	img3 = models.ImageField(upload_to='Project', blank=True)
	img4 = models.ImageField(upload_to='Project', blank=True)

	def __str__(self):
		return self.title


class Cold_welding_project9(models.Model):
	title = models.CharField(max_length=500, default='', blank=True )
	text = models.CharField(max_length=500, default='', blank=True ,null=True)
	img1 = models.ImageField(upload_to='Project', blank=True)
	img2 = models.ImageField(upload_to='Project', blank=True)
	img3 = models.ImageField(upload_to='Project', blank=True)
	img4 = models.ImageField(upload_to='Project', blank=True)

	def __str__(self):
		return self.title


class Cold_welding_project10(models.Model):
	title = models.CharField(max_length=500, default='', blank=True )
	text = models.CharField(max_length=500, default='', blank=True ,null=True)
	img1 = models.ImageField(upload_to='Project', blank=True)
	img2 = models.ImageField(upload_to='Project', blank=True)
	img3 = models.ImageField(upload_to='Project', blank=True)
	img4 = models.ImageField(upload_to='Project', blank=True)

	def __str__(self):
		return self.title


class Cold_welding_project11(models.Model):
	title = models.CharField(max_length=500, default='', blank=True )
	text = models.CharField(max_length=500, default='', blank=True ,null=True)
	img1 = models.ImageField(upload_to='Project', blank=True)
	img2 = models.ImageField(upload_to='Project', blank=True)
	img3 = models.ImageField(upload_to='Project', blank=True)
	img4 = models.ImageField(upload_to='Project', blank=True)

	def __str__(self):
		return self.title


class Cold_welding_project12(models.Model):
	title = models.CharField(max_length=500, default='', blank=True )
	text = models.CharField(max_length=500, default='', blank=True ,null=True)
	img1 = models.ImageField(upload_to='Project', blank=True)
	img2 = models.ImageField(upload_to='Project', blank=True)
	img3 = models.ImageField(upload_to='Project', blank=True)
	img4 = models.ImageField(upload_to='Project', blank=True)

	def __str__(self):
		return self.title


class Cold_welding_project13(models.Model):
	title = models.CharField(max_length=500, default='', blank=True )
	text = models.CharField(max_length=500, default='', blank=True ,null=True)
	img1 = models.ImageField(upload_to='Project', blank=True)
	img2 = models.ImageField(upload_to='Project', blank=True)
	img3 = models.ImageField(upload_to='Project', blank=True)
	img4 = models.ImageField(upload_to='Project', blank=True)

	def __str__(self):
		return self.title


class Cold_welding_project14(models.Model):
	title = models.CharField(max_length=500, default='', blank=True )
	text = models.CharField(max_length=500, default='', blank=True ,null=True)
	img1 = models.ImageField(upload_to='Project', blank=True)
	img2 = models.ImageField(upload_to='Project', blank=True)
	img3 = models.ImageField(upload_to='Project', blank=True)
	img4 = models.ImageField(upload_to='Project', blank=True)

	def __str__(self):
		return self.title


class Cold_welding_project15(models.Model):
	title = models.CharField(max_length=500, default='', blank=True )
	text = models.CharField(max_length=500, default='', blank=True ,null=True)
	img1 = models.ImageField(upload_to='Project', blank=True)
	img2 = models.ImageField(upload_to='Project', blank=True)
	img3 = models.ImageField(upload_to='Project', blank=True)
	img4 = models.ImageField(upload_to='Project', blank=True)

	def __str__(self):
		return self.title


class Cold_welding_project16(models.Model):
	title = models.CharField(max_length=500, default='', blank=True )
	text = models.CharField(max_length=500, default='', blank=True ,null=True)
	img1 = models.ImageField(upload_to='Project', blank=True)
	img2 = models.ImageField(upload_to='Project', blank=True)
	img3 = models.ImageField(upload_to='Project', blank=True)
	img4 = models.ImageField(upload_to='Project', blank=True)

	def __str__(self):
		return self.title


class Cold_welding_project17(models.Model):
	title = models.CharField(max_length=500, default='', blank=True )
	text = models.CharField(max_length=500, default='', blank=True ,null=True)
	img1 = models.ImageField(upload_to='Project', blank=True)
	img2 = models.ImageField(upload_to='Project', blank=True)
	img3 = models.ImageField(upload_to='Project', blank=True)
	img4 = models.ImageField(upload_to='Project', blank=True)

	def __str__(self):
		return self.title


class Cold_welding_project18(models.Model):
	title = models.CharField(max_length=500, default='', blank=True )
	text = models.CharField(max_length=500, default='', blank=True ,null=True)
	img1 = models.ImageField(upload_to='Project', blank=True)
	img2 = models.ImageField(upload_to='Project', blank=True)
	img3 = models.ImageField(upload_to='Project', blank=True)
	img4 = models.ImageField(upload_to='Project', blank=True)

	def __str__(self):
		return self.title


class Cold_welding_project19(models.Model):
	title = models.CharField(max_length=500, default='', blank=True )
	text = models.CharField(max_length=500, default='', blank=True ,null=True)
	img1 = models.ImageField(upload_to='Project', blank=True)
	img2 = models.ImageField(upload_to='Project', blank=True)
	img3 = models.ImageField(upload_to='Project', blank=True)
	img4 = models.ImageField(upload_to='Project', blank=True)

	def __str__(self):
		return self.title


class Cold_welding_project20(models.Model):
	title = models.CharField(max_length=500, default='', blank=True )
	text = models.CharField(max_length=500, default='', blank=True ,null=True)
	img1 = models.ImageField(upload_to='Project', blank=True)
	img2 = models.ImageField(upload_to='Project', blank=True)
	img3 = models.ImageField(upload_to='Project', blank=True)
	img4 = models.ImageField(upload_to='Project', blank=True)

	def __str__(self):
		return self.title














#-------------------------------------------------------------------------

class penetrant_test(models.Model):
	title = models.CharField(max_length=500, default='', blank=True )
	text = models.CharField(max_length=500, default='', blank=True ,null=True)
	img1 = models.ImageField(upload_to='Project', blank=True)
	img2 = models.ImageField(upload_to='Project', blank=True)

	def __str__(self):
		return self.title


class Epcco_NDT_test(models.Model):
	title = models.CharField(max_length=500, default='', blank=True )
	text = models.CharField(max_length=500, default='', blank=True ,null=True)
	img1 = models.ImageField(upload_to='Project', blank=True)
	img2 = models.ImageField(upload_to='Project', blank=True)
	img3 = models.ImageField(upload_to='Project', blank=True)
	img4 = models.ImageField(upload_to='Project', blank=True)

	def __str__(self):
		return self.title


class Ultra_sonic(models.Model):
	title = models.CharField(max_length=500, default='', blank=True )
	text = models.CharField(max_length=500, default='', blank=True ,null=True)
	img1 = models.ImageField(upload_to='Project', blank=True)
	img2 = models.ImageField(upload_to='Project', blank=True)
	img3 = models.ImageField(upload_to='Project', blank=True)
	img4 = models.ImageField(upload_to='Project', blank=True)

	def __str__(self):
		return self.title
