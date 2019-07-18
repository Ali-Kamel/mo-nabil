from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.index,name='home'),
    path('about/',views.about ,name='about'),
    path('contact/',views.contact ,name='contact'),
    path('contact-info/',views.contactinformation ,name='contactinfo'),
    path('news/',views.news ,name='news'),
    path('events/',views.events ,name='events'),
    path('our-team/',views.ourteam ,name='ourteam'),
    # path('Services/Manufacture_and_maintenance_of_marine_Ships',views.manufacture ,name='Manufacture'),




























    path('Services/Construction/Steel-Structure/fubrication-and-errection-of-steel-structure',views.view1 ,name='url1'),
    path('Services/Construction/Steel-Structure/fabrication-and-coating',views.view2 ,name='url2'),

    path('Services/Construction/Marine-structure/Manufacture-and-maintenance',views.view3 ,name='url3'),
    path('Services/Construction/Marine-structure/Construction-and-repair',views.view4 ,name='url4'),

    path('Services/Construction/Piping/Oil-tank-fire',views.view5 ,name='url5'),
    path('Services/Construction/Piping/Piping-construction',views.view6 ,name='url6'),
    path('Services/Construction/Piping/Piping-construction2',views.view7 ,name='url7'),

    path('Services/Construction/Vassel&Tanks/Ammonia-spherical-tank-maintenance',views.view8 ,name='url8'),
    path('Services/Construction/Vassel&Tanks/Copper-heat-exchanger',views.view9 ,name='url9'),
    path('Services/Construction/Vassel&Tanks/Dismandteling-and-reconstruction',views.view10 ,name='url10'),
    path('Services/Construction/Vassel&Tanks/Dismantle-a-waste-heat-boiler',views.view11 ,name='url11'),
    path('Services/Construction/Vassel&Tanks/Maintenance-of-heat-exchangers',views.view12 ,name='url12'),
    path('Services/Construction/Vassel&Tanks/Heat-exchanger-repair',views.view13 ,name='url13'),
    path('Services/Construction/Vassel&Tanks/Retubing-heat-exchanger',views.view14 ,name='url14'),
    path('Services/Construction/Vassel&Tanks/Tanks-Fabrication',views.view15 ,name='url15'),
    path('Services/Construction/Vassel&Tanks/Titanium-tube-at-nitric-acid-plant',views.view16 ,name='url16'),

    path('Services/Wear-abrasion/Hard-plates/Manufacture-of-hard-wear-cone',views.view17 ,name='url17'),
    path('Services/Wear-abrasion/Hard-facing/Selection-of-the-suitable-hard-facing-electrocle',views.view18 ,name='url18'),

    path('Services/Heavy-trucky/Maintenance-of-heavy-trucks-structure',views.view19 ,name='url19'),
    path('Services/Heavy-trucky/Manufacture-and-welding-of-heads-of-heavy-trucks',views.view20 ,name='url20'),
    path('Services/Heavy-trucky/Repair-of-damaged-hydrolic-pislon-of-loader',views.view21 ,name='url21'),
    path('Services/Heavy-trucky/Repair-of-treated-and-cracked-loader-bucket',views.view22 ,name='url22'),
    path('Services/Heavy-trucky/Welding-repair-of-heavy-truck-rims',views.view23 ,name='url23'),


    path('Services/Welding/Corbon-Steel-Welding-and-repair/Dismanteling-old-expansion-joint',views.view24 ,name='url24'),
    path('Services/Welding/Corbon-Steel-Welding-and-repair/Dismanteling-the-DRI-reactor-spod',views.view25 ,name='url25'),

    path('Services/Welding/Stainless-steel-Welding-and-repair/Compressor-housing-ss304-repair',views.view26 ,name='url26'),
    path('Services/Welding/Stainless-steel-Welding-and-repair/Replacement-of-the-second-stage-of-nitricacid-lower-ss304L',views.view27 ,name='url27'),
    path('Services/Welding/Stainless-steel-Welding-and-repair/Welding-repair-ss304H-tube-cladded-innerly',views.view28 ,name='url28'),

    path('Services/Welding/Cast-iron-Welding-and-repair/Welding-of-Broken-and-cracked-parts-for-cast-iron-pump-housing',views.view29 ,name='url29'),
    path('Services/Welding/Cast-iron-Welding-and-repair/Welding-of-Broken-and-cracked-parts-for-cast=iron-pump-housing-2',views.view30 ,name='url30'),

    path('Services/Welding/Copper-Welding-and-repair/Project-1',views.view31 ,name='url31'),
    path('Services/Welding/Copper-Welding-and-repair/Project-2',views.view32 ,name='url32'),

    path('Services/Welding/Aluminume-welding-and-repair/project-1',views.view33 ,name='url33'),
    path('Services/Welding/Aluminume-welding-and-repair/project-2',views.view34 ,name='url34'),

    path('Services/Welding/Nical-base-alloy/Dismanteling-and-welding-repair-of-reformer-incoloy-800-tube',views.view35 ,name='url35'),
    path('Services/Welding/Nical-base-alloy/Repair-of-incolloy-800-header-of-reforme-at-amonia',views.view36 ,name='url36'),



    path('Services/Cold-welding/project1',views.view37 ,name='url37'),
    path('Services/Cold-welding/project2',views.view38 ,name='url38'),
    path('Services/Cold-welding/project3',views.view39 ,name='url39'),
    path('Services/Cold-welding/project4',views.view40 ,name='url40'),
    path('Services/Cold-welding/project5',views.view41 ,name='url41'),
    path('Services/Cold-welding/project6',views.view42 ,name='url42'),
    path('Services/Cold-welding/project7',views.view43 ,name='url43'),
    path('Services/Cold-welding/project8',views.view44 ,name='url44'),
    path('Services/Cold-welding/project9',views.view45 ,name='url45'),
    path('Services/Cold-welding/project10',views.view46 ,name='url46'),
    path('Services/Cold-welding/project11',views.view47 ,name='url47'),
    path('Services/Cold-welding/project12',views.view48 ,name='url48'),
    path('Services/Cold-welding/project13',views.view49 ,name='url49'),
    path('Services/Cold-welding/project14',views.view50 ,name='url50'),
    path('Services/Cold-welding/project15',views.view51 ,name='url51'),
    path('Services/Cold-welding/project16',views.view52 ,name='url52'),
    path('Services/Cold-welding/project17',views.view53 ,name='url53'),
    path('Services/Cold-welding/project18',views.view54 ,name='url54'),
    path('Services/Cold-welding/project19',views.view55 ,name='url55'),
    path('Services/Cold-welding/project20',views.view56 ,name='url56'),

    path('Services/Non-Destructive-test/penetrant-test',views.view57 ,name='url57'),
    path('Services/Non-Destructive-test/Epcco-NDT-test',views.view58 ,name='url58'),
    path('Services/Non-Destructive-test/Ultra-sonic',views.view59 ,name='url59')


]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns+= static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
