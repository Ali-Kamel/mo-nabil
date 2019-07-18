from django.shortcuts import render
from Code.models import *
from django.core.mail import send_mail
from Code.forms import Email




def email(request):
	pass
	# send_mail('Hello from EPPCO',
	# 'Test Email !!',
	# 'sent from email'
	# 'sent to email'
	# fail_silently=False)

def index(request):
	Service = homeproject.objects.all()
	args = {'homeproject': Service}
	return render(request,'home/index.html',args)


def contact(request):
	if request.method == 'GET':
		form = Email()
	else:
		form = Email()
	return render(request,'home/contact.html',{"form":form})


def about(request):
	About = aboutus.objects.all()
	args = {'aboutus': About}
	return render(request,'home/about.html',args)

	
def contactinformation(request):
	Contact = contactinfo.objects.all()
	args = {'contactinfo': Contact}
	return render(request,'home/contactinfo.html',args)


def news(request):
	return render(request,'home/news.html')


def events(request):
	About = eventi.objects.all()
	args = {'Manufacture': About}
	return render(request,'home/events.html',args)


def ourteam(request):
	return render(request,'home/ourteam.html')


# def manufacture(request):
# 	About = Manufacture.objects.all()
# 	args = {'Manufacture': About}
# 	return render(request,'home/Manufacture.html',args)












































def view1(request):
	About = fubrication_errection_of_steel_structure.objects.all()
	args = {'Manufacture': About}
	return render(request,'service/fubrication_errection_of_steel_structure.html',args)


def view2(request):
	About = fabrication_and_coating.objects.all()
	args = {'Manufacture': About}
	return render(request,'service/fabrication_and_coating.html',args)
#-----------------------------------------------------------------------------------------

def view3(request):
	About = Manufacture_and_maintenance.objects.all()
	args = {'Manufacture': About}
	return render(request,'service/Manufacture_and_maintenance.html',args)


def view4(request):
	About = Construction_and_repair.objects.all()
	args = {'Manufacture': About}
	return render(request,'service/Construction_and_repair.html',args)

#-----------------------------------------------------------------------------------------
def view5(request):
	About = Oil_tank_fire.objects.all()
	args = {'Manufacture': About}
	return render(request,'service/Oil_tank_fire.html',args)


def view6(request):
	About = Piping_construction.objects.all()
	args = {'Manufacture': About}
	return render(request,'service/Piping_construction.html',args)


def view7(request):
	About = Piping_construction2.objects.all()
	args = {'Manufacture': About}
	return render(request,'service/Piping_construction2.html',args)

#-----------------------------------------------------------------------------------------
def view8(request):
	About = Ammonia_spherical_tank_maintenance.objects.all()
	args = {'Manufacture': About}
	return render(request,'service/Ammonia_spherical_tank_maintenance.html',args)


def view9(request):
	About = Copper_heat_exchanger.objects.all()
	args = {'Manufacture': About}
	return render(request,'service/Copper_heat_exchanger.html',args)


def view10(request):
	About = Dismandteling_and_reconstruction.objects.all()
	args = {'Manufacture': About}
	return render(request,'service/Dismandteling_and_reconstruction.html',args)


def view11(request):
	About = Dismantle_a_waste_heat_boiler.objects.all()
	args = {'Manufacture': About}
	return render(request,'service/Dismantle_a_waste_heat_boiler.html',args)


def view12(request):
	About = Maintenance_of_heat_exchangers.objects.all()
	args = {'Manufacture': About}
	return render(request,'service/Maintenance_of_heat_exchangers.html',args)


def view13(request):
	About = Heat_exchanger_repair.objects.all()
	args = {'Manufacture': About}
	return render(request,'service/Heat_exchanger_repair.html',args)


def view14(request):
	About = Retubing_heat_exchanger.objects.all()
	args = {'Manufacture': About}
	return render(request,'service/Retubing_heat_exchanger.html',args)


def view15(request):
	About = Tanks_Fabrication.objects.all()
	args = {'Manufacture': About}
	return render(request,'service/Tanks_Fabrication.html',args)


def view16(request):
	About = Titanium_tube_at_nitric_acid_plant.objects.all()
	args = {'Manufacture': About}
	return render(request,'service/Titanium_tube_at_nitric_acid_plant.html',args)
#-----------------------------------------------------------------------------------------

def view17(request):
	About = Manufacture_of_hard_wear_core.objects.all()
	args = {'Manufacture': About}
	return render(request,'service/Manufacture_of_hard_wear_core.html',args)


def view18(request):
	About = Selection_of_the_suitable_hard_facing_electrocle.objects.all()
	args = {'Manufacture': About}
	return render(request,'service/Selection_of_the_suitable_hard_facing_electrocle.html',args)
#-----------------------------------------------------------------------------------------

def view19(request):
	About = Maintenance_of_heavy_trucks_structure.objects.all()
	args = {'Manufacture': About}
	return render(request,'service/Maintenance_of_heavy_trucks_structure.html',args)


def view20(request):
	About = Manufacture_and_welding_of_heads_of_heavy_trucks.objects.all()
	args = {'Manufacture': About}
	return render(request,'service/Manufacture_and_welding_of_heads_of_heavy_trucks.html',args)


def view21(request):
	About = Repair_of_damaged_hydrolic_pislon_of_loader.objects.all()
	args = {'Manufacture': About}
	return render(request,'service/Repair_of_damaged_hydrolic_pislon_of_loader.html',args)



def view22(request):
	About = Repair_of_treated_and_cracked_loader_bucket.objects.all()
	args = {'Manufacture': About}
	return render(request,'service/Repair_of_treated_and_cracked_loader_bucket.html',args)


def view23(request):
	About = Welding_repair_of_heavy_truck_rims.objects.all()
	args = {'Manufacture': About}
	return render(request,'service/Welding_repair_of_heavy_truck_rims.html',args)
#-----------------------------------------------------------------------------------------

def view24(request):
	About = Dismanteling_old_expansion_joint.objects.all()
	args = {'Manufacture': About}
	return render(request,'service/Dismanteling_old_expansion_joint.html',args)


def view25(request):
	About = Dismanteling_the_DRI_reactor_spod.objects.all()
	args = {'Manufacture': About}
	return render(request,'service/Dismanteling_the_DRI_reactor_spod.html',args)

#-----------------------------------------------------------------------------------------
def view26(request):
	About = Compressor_housing_ss304_repair.objects.all()
	args = {'Manufacture': About}
	return render(request,'service/Compressor_housing_ss304_repair.html',args)


def view27(request):
	About = Replacement_of_the_second_stage_of_nitricacid_lower_ss304L.objects.all()
	args = {'Manufacture': About}
	return render(request,'service/Replacement_of_the_second_stage_of_nitricacid_lower_ss304L.html',args)


def view28(request):
	About = Welding_repair_ss304H_tube_cladded_innerly.objects.all()
	args = {'Manufacture': About}
	return render(request,'service/Welding_repair_ss304H_tube_cladded_innerly.html',args)

#-----------------------------------------------------------------------------------------
def view29(request):
	About = Welding_of_Broken_and_cracked_parts_for_cast_iron_pump_housing.objects.all()
	args = {'Manufacture': About}
	return render(request,'service/Welding_of_Broken_and_cracked_parts_for_cast_iron_pump_housing.html',args)


def view30(request):
	About = Welding_of_Broken_and_cracked_parts_for_cast_iron_pump_housing2.objects.all()
	args = {'Manufacture': About}
	return render(request,'service/Welding_of_Broken_and_cracked_parts_for_cast_iron_pump_housing2.html',args)

#-----------------------------------------------------------------------------------------
def view31(request):
	About = Copper_Welding_Project_1.objects.all()
	args = {'Manufacture': About}
	return render(request,'service/Copper_Welding_Project_1.html',args)


def view32(request):
	About = Copper_Welding_Project_2.objects.all()
	args = {'Manufacture': About}
	return render(request,'service/Copper_Welding_Project_2.html',args)

#-----------------------------------------------------------------------------------------
def view33(request):
	About = Aluminume_welding_project_1.objects.all()
	args = {'Manufacture': About}
	return render(request,'service/Aluminume_welding_project_1.html',args)


def view34(request):
	About = Aluminume_welding_project_2.objects.all()
	args = {'Manufacture': About}
	return render(request,'service/Aluminume_welding_project_2.html',args)
#-----------------------------------------------------------------------------------------

def view35(request):
	About = Dismanteling_and_welding_repair_of_reformer_incoloy_800_tube.objects.all()
	args = {'Manufacture': About}
	return render(request,'service/Dismanteling_and_welding_repair_of_reformer_incoloy_800_tube.html',args)


def view36(request):
	About = Repair_of_incolloy_800_header_of_reforme_at_amonia.objects.all()
	args = {'Manufacture': About}
	return render(request,'service/Repair_of_incolloy_800_header_of_reforme_at_amonia.html',args)

#-----------------------------------------------------------------------------------------
def view37(request):
	About = Cold_welding_project1.objects.all()
	args = {'Manufacture': About}
	return render(request,'service/Cold_welding_project1.html',args)


def view38(request):
	About = Cold_welding_project2.objects.all()
	args = {'Manufacture': About}
	return render(request,'service/Cold_welding_project2.html',args)


def view39(request):
	About = Cold_welding_project3.objects.all()
	args = {'Manufacture': About}
	return render(request,'service/Cold_welding_project3.html',args)


def view40(request):
	About = Cold_welding_project4.objects.all()
	args = {'Manufacture': About}
	return render(request,'service/Cold_welding_project4.html',args)


def view41(request):
	About = Cold_welding_project5.objects.all()
	args = {'Manufacture': About}
	return render(request,'service/Cold_welding_project5.html',args)

def view42(request):
	About = Cold_welding_project6.objects.all()
	args = {'Manufacture': About}
	return render(request,'service/Cold_welding_project6.html',args)


def view43(request):
	About = Cold_welding_project7.objects.all()
	args = {'Manufacture': About}
	return render(request,'service/Cold_welding_project7.html',args)


def view44(request):
	About = Cold_welding_project8.objects.all()
	args = {'Manufacture': About}
	return render(request,'service/Cold_welding_project8.html',args)


def view45(request):
	About = Cold_welding_project9.objects.all()
	args = {'Manufacture': About}
	return render(request,'service/Cold_welding_project9.html',args)


def view46(request):
	About = Cold_welding_project10.objects.all()
	args = {'Manufacture': About}
	return render(request,'service/Cold_welding_project10.html',args)


def view47(request):
	About = Cold_welding_project11.objects.all()
	args = {'Manufacture': About}
	return render(request,'service/Cold_welding_project11.html',args)


def view48(request):
	About = Cold_welding_project12.objects.all()
	args = {'Manufacture': About}
	return render(request,'service/Cold_welding_project12.html',args)


def view49(request):
	About = Cold_welding_project13.objects.all()
	args = {'Manufacture': About}
	return render(request,'service/Cold_welding_project13.html',args)


def view50(request):
	About = Cold_welding_project14.objects.all()
	args = {'Manufacture': About}
	return render(request,'service/Cold_welding_project14.html',args)


def view51(request):
	About = Cold_welding_project15.objects.all()
	args = {'Manufacture': About}
	return render(request,'service/Cold_welding_project15.html',args)


def view52(request):
	About = Cold_welding_project16.objects.all()
	args = {'Manufacture': About}
	return render(request,'service/Cold_welding_project16.html',args)


def view53(request):
	About = Cold_welding_project17.objects.all()
	args = {'Manufacture': About}
	return render(request,'service/Cold_welding_project17.html',args)


def view54(request):
	About = Cold_welding_project18.objects.all()
	args = {'Manufacture': About}
	return render(request,'service/Cold_welding_project18.html',args)


def view55(request):
	About = Cold_welding_project19.objects.all()
	args = {'Manufacture': About}
	return render(request,'service/Cold_welding_project19.html',args)


def view56(request):
	About = Cold_welding_project20.objects.all()
	args = {'Manufacture': About}
	return render(request,'service/Cold_welding_project20.html',args)
#-------------------------------------------------------------------------

def view57(request):
	About = penetrant_test.objects.all()
	args = {'Manufacture': About}
	return render(request,'service/penetrant_test.html',args)


def view58(request):
	About = Epcco_NDT_test.objects.all()
	args = {'Manufacture': About}
	return render(request,'service/Epcco_NDT_test.html',args)


def view59(request):
	About = Ultra_sonic.objects.all()
	args = {'Manufacture': About}
	return render(request,'service/Ultra_sonic.html',args)