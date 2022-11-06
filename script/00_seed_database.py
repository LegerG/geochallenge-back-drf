#!/usr/bin/env python
import json
from flagschallenge.models import Territory, TerritoryName, Language, TerritoryGroup, GeographyBase


def main() -> None:
    """Main entry point of the app."""

    # Delete all data
    GeographyBase.objects.all().delete()
    Territory.objects.all().delete()
    TerritoryName.objects.all().delete()
    Language.objects.all().delete()
    TerritoryGroup.objects.all().delete()

    # Create supported languages
    Language.objects.create(code="en", name="English")
    Language.objects.create(code="fr", name="Français")
    Language.objects.create(code="de", name="Deutsch")
    Language.objects.create(code="es", name="Español")
    Language.objects.create(code="it", name="Italiano")

    # Create continents
    africa = TerritoryGroup.objects.create(
        code="gr_af", wikipedia_link="https://en.wikipedia.org/wiki/Africa")
    asia = TerritoryGroup.objects.create(
        code="gr_as", wikipedia_link="https://en.wikipedia.org/wiki/Asia")
    europa = TerritoryGroup.objects.create(
        code="gr_eu", wikipedia_link="https://en.wikipedia.org/wiki/Europe")
    north_america = TerritoryGroup.objects.create(
        code="gr_na", wikipedia_link="https://en.wikipedia.org/wiki/North_America")
    oceania = TerritoryGroup.objects.create(
        code="gr_oc", wikipedia_link="https://en.wikipedia.org/wiki/Oceania")
    south_america = TerritoryGroup.objects.create(
        code="gr_sa", wikipedia_link="https://en.wikipedia.org/wiki/South_America")
    antarctica = TerritoryGroup.objects.create(
        code="gr_an", wikipedia_link="https://en.wikipedia.org/wiki/Antarctica")

    # Create countries

    #    ▄████████    ▄████████  ▄█     ▄████████
    #   ███    ███   ███    ███ ███    ███    ███
    #   ███    ███   ███    █▀  ███▌   ███    ███
    #   ███    ███   ███        ███▌   ███    ███
    # ▀███████████ ▀███████████ ███▌ ▀███████████
    #   ███    ███          ███ ███    ███    ███
    #   ███    ███    ▄█    ███ ███    ███    ███
    #   ███    █▀   ▄████████▀  █▀     ███    █▀

    Territory.objects.create(
        code="io", wikipedia_link="https://en.wikipedia.org/wiki/British_Indian_Ocean_Territory").groups.add(asia)
    Territory.objects.create(
        code="sg", wikipedia_link="https://en.wikipedia.org/wiki/Singapore").groups.add(asia)
    Territory.objects.create(
        code="mm", wikipedia_link="https://en.wikipedia.org/wiki/Myanmar").groups.add(asia)
    Territory.objects.create(
        code="cc", wikipedia_link="https://en.wikipedia.org/wiki/Cocos_(Keeling)_Islands").groups.add(asia)
    Territory.objects.create(
        code="np", wikipedia_link="https://en.wikipedia.org/wiki/Nepal").groups.add(asia)
    Territory.objects.create(
        code="kp", wikipedia_link="https://en.wikipedia.org/wiki/North_Korea").groups.add(asia)
    Territory.objects.create(
        code="sy", wikipedia_link="https://en.wikipedia.org/wiki/Syria").groups.add(asia)
    Territory.objects.create(
        code="id", wikipedia_link="https://en.wikipedia.org/wiki/Indonesia").groups.add(asia)
    Territory.objects.create(
        code="kz", wikipedia_link="https://en.wikipedia.org/wiki/Kazakhstan").groups.add(asia)
    Territory.objects.create(
        code="jp", wikipedia_link="https://en.wikipedia.org/wiki/Japan").groups.add(asia)
    Territory.objects.create(
        code="ps", wikipedia_link="https://en.wikipedia.org/wiki/State_of_Palestine").groups.add(asia)
    Territory.objects.create(
        code="kg", wikipedia_link="https://en.wikipedia.org/wiki/Kyrgyzstan").groups.add(asia)
    Territory.objects.create(
        code="iq", wikipedia_link="https://en.wikipedia.org/wiki/Iraq").groups.add(asia)
    Territory.objects.create(
        code="lb", wikipedia_link="https://en.wikipedia.org/wiki/Lebanon").groups.add(asia)
    Territory.objects.create(
        code="bn", wikipedia_link="https://en.wikipedia.org/wiki/Brunei").groups.add(asia)
    Territory.objects.create(
        code="tm", wikipedia_link="https://en.wikipedia.org/wiki/Turkmenistan").groups.add(asia)
    Territory.objects.create(
        code="lk", wikipedia_link="https://en.wikipedia.org/wiki/Sri_Lanka").groups.add(asia)
    Territory.objects.create(
        code="kh", wikipedia_link="https://en.wikipedia.org/wiki/Cambodia").groups.add(asia)
    Territory.objects.create(
        code="bd", wikipedia_link="https://en.wikipedia.org/wiki/Bangladesh").groups.add(asia)
    Territory.objects.create(
        code="ae", wikipedia_link="https://en.wikipedia.org/wiki/United_Arab_Emirates").groups.add(asia)
    Territory.objects.create(
        code="ye", wikipedia_link="https://en.wikipedia.org/wiki/Yemen").groups.add(asia)
    Territory.objects.create(
        code="qa", wikipedia_link="https://en.wikipedia.org/wiki/Qatar").groups.add(asia)
    Territory.objects.create(
        code="om", wikipedia_link="https://en.wikipedia.org/wiki/Oman").groups.add(asia)
    Territory.objects.create(
        code="ge", wikipedia_link="https://en.wikipedia.org/wiki/Georgia_(country)").groups.add(asia)
    Territory.objects.create(
        code="mn", wikipedia_link="https://en.wikipedia.org/wiki/Mongolia").groups.add(asia)
    Territory.objects.create(
        code="vn", wikipedia_link="https://en.wikipedia.org/wiki/Vietnam").groups.add(asia)
    Territory.objects.create(
        code="mo", wikipedia_link="https://en.wikipedia.org/wiki/Macau").groups.add(asia)
    Territory.objects.create(
        code="tj", wikipedia_link="https://en.wikipedia.org/wiki/Tajikistan").groups.add(asia)
    Territory.objects.create(
        code="am", wikipedia_link="https://en.wikipedia.org/wiki/Armenia").groups.add(asia)
    Territory.objects.create(
        code="il", wikipedia_link="https://en.wikipedia.org/wiki/Israel").groups.add(asia)
    Territory.objects.create(
        code="jo", wikipedia_link="https://en.wikipedia.org/wiki/Jordan").groups.add(asia)
    Territory.objects.create(
        code="ir", wikipedia_link="https://en.wikipedia.org/wiki/Iran").groups.add(asia)
    Territory.objects.create(
        code="kr", wikipedia_link="https://en.wikipedia.org/wiki/South_Korea").groups.add(asia)
    Territory.objects.create(
        code="tr", wikipedia_link="https://en.wikipedia.org/wiki/Turkey").groups.add(asia)
    Territory.objects.create(
        code="bt", wikipedia_link="https://en.wikipedia.org/wiki/Bhutan").groups.add(asia)
    Territory.objects.create(
        code="hk", wikipedia_link="https://en.wikipedia.org/wiki/Hong_Kong").groups.add(asia)
    Territory.objects.create(
        code="az", wikipedia_link="https://en.wikipedia.org/wiki/Azerbaijan").groups.add(asia)
    Territory.objects.create(
        code="th", wikipedia_link="https://en.wikipedia.org/wiki/Thailand").groups.add(asia)
    Territory.objects.create(
        code="tw", wikipedia_link="https://en.wikipedia.org/wiki/Taiwan").groups.add(asia)
    Territory.objects.create(
        code="in", wikipedia_link="https://en.wikipedia.org/wiki/India").groups.add(asia)
    Territory.objects.create(
        code="la", wikipedia_link="https://en.wikipedia.org/wiki/Laos").groups.add(asia)
    Territory.objects.create(
        code="af", wikipedia_link="https://en.wikipedia.org/wiki/Afghanistan").groups.add(asia)
    Territory.objects.create(
        code="tl", wikipedia_link="https://en.wikipedia.org/wiki/East_Timor").groups.add(asia)
    Territory.objects.create(
        code="sa", wikipedia_link="https://en.wikipedia.org/wiki/Saudi_Arabia").groups.add(asia)
    Territory.objects.create(
        code="bh", wikipedia_link="https://en.wikipedia.org/wiki/Bahrain").groups.add(asia)
    Territory.objects.create(
        code="mv", wikipedia_link="https://en.wikipedia.org/wiki/Maldives").groups.add(asia)
    Territory.objects.create(
        code="kw", wikipedia_link="https://en.wikipedia.org/wiki/Kuwait").groups.add(asia)
    Territory.objects.create(
        code="pk", wikipedia_link="https://en.wikipedia.org/wiki/Pakistan").groups.add(asia)
    Territory.objects.create(
        code="cn", wikipedia_link="https://en.wikipedia.org/wiki/China").groups.add(asia)
    Territory.objects.create(
        code="ph", wikipedia_link="https://en.wikipedia.org/wiki/Philippines").groups.add(asia)
    Territory.objects.create(
        code="cy", wikipedia_link="https://en.wikipedia.org/wiki/Cyprus").groups.add(asia)
    Territory.objects.create(
        code="uz", wikipedia_link="https://en.wikipedia.org/wiki/Uzbekistan").groups.add(asia)
    Territory.objects.create(
        code="my", wikipedia_link="https://en.wikipedia.org/wiki/Malaysia").groups.add(asia)

    #    ▄████████ ███    █▄     ▄████████  ▄██████▄     ▄███████▄    ▄████████
    #   ███    ███ ███    ███   ███    ███ ███    ███   ███    ███   ███    ███
    #   ███    █▀  ███    ███   ███    ███ ███    ███   ███    ███   ███    ███
    #  ▄███▄▄▄     ███    ███  ▄███▄▄▄▄██▀ ███    ███   ███    ███   ███    ███
    # ▀▀███▀▀▀     ███    ███ ▀▀███▀▀▀▀▀   ███    ███ ▀█████████▀  ▀███████████
    #   ███    █▄  ███    ███ ▀███████████ ███    ███   ███          ███    ███
    #   ███    ███ ███    ███   ███    ███ ███    ███   ███          ███    ███
    #   ██████████ ████████▀    ███    ███  ▀██████▀   ▄████▀        ███    █▀
    #                           ███    ███

    Territory.objects.create(
        code="sk", wikipedia_link="https://en.wikipedia.org/wiki/Slovakia").groups.add(europa)
    Territory.objects.create(
        code="li", wikipedia_link="https://en.wikipedia.org/wiki/Liechtenstein").groups.add(europa)
    Territory.objects.create(
        code="be", wikipedia_link="https://en.wikipedia.org/wiki/Belgium").groups.add(europa)
    Territory.objects.create(
        code="dk", wikipedia_link="https://en.wikipedia.org/wiki/Denmark").groups.add(europa)
    Territory.objects.create(
        code="xk", wikipedia_link="https://en.wikipedia.org/wiki/Kosovo").groups.add(europa)
    Territory.objects.create(
        code="hr", wikipedia_link="https://en.wikipedia.org/wiki/Croatia").groups.add(europa)
    Territory.objects.create(
        code="ba", wikipedia_link="https://en.wikipedia.org/wiki/Bosnia_and_Herzegovina").groups.add(europa)
    Territory.objects.create(
        code="im", wikipedia_link="https://en.wikipedia.org/wiki/Isle_of_Man").groups.add(europa)
    Territory.objects.create(
        code="rs", wikipedia_link="https://en.wikipedia.org/wiki/Serbia").groups.add(europa)
    Territory.objects.create(
        code="no", wikipedia_link="https://en.wikipedia.org/wiki/Norway").groups.add(europa)
    Territory.objects.create(
        code="nl", wikipedia_link="https://en.wikipedia.org/wiki/Netherlands").groups.add(europa)
    Territory.objects.create(
        code="lt", wikipedia_link="https://en.wikipedia.org/wiki/Lithuania").groups.add(europa)
    Territory.objects.create(
        code="fr", wikipedia_link="https://en.wikipedia.org/wiki/France").groups.add(europa)
    Territory.objects.create(
        code="ru", wikipedia_link="https://en.wikipedia.org/wiki/Russia").groups.add(europa)
    Territory.objects.create(
        code="cz", wikipedia_link="https://en.wikipedia.org/wiki/Czech_Republic").groups.add(europa)
    Territory.objects.create(
        code="ee", wikipedia_link="https://en.wikipedia.org/wiki/Estonia").groups.add(europa)
    Territory.objects.create(
        code="va", wikipedia_link="https://en.wikipedia.org/wiki/Vatican_City").groups.add(europa)
    Territory.objects.create(
        code="ie", wikipedia_link="https://en.wikipedia.org/wiki/Ireland").groups.add(europa)
    Territory.objects.create(
        code="es", wikipedia_link="https://en.wikipedia.org/wiki/Spain").groups.add(europa)
    Territory.objects.create(
        code="pl", wikipedia_link="https://en.wikipedia.org/wiki/Poland").groups.add(europa)
    Territory.objects.create(
        code="lu", wikipedia_link="https://en.wikipedia.org/wiki/Luxembourg").groups.add(europa)
    Territory.objects.create(
        code="at", wikipedia_link="https://en.wikipedia.org/wiki/Austria").groups.add(europa)
    Territory.objects.create(
        code="mc", wikipedia_link="https://en.wikipedia.org/wiki/Monaco").groups.add(europa)
    Territory.objects.create(
        code="gr", wikipedia_link="https://en.wikipedia.org/wiki/Greece").groups.add(europa)
    Territory.objects.create(
        code="si", wikipedia_link="https://en.wikipedia.org/wiki/Slovenia").groups.add(europa)
    Territory.objects.create(
        code="al", wikipedia_link="https://en.wikipedia.org/wiki/Albania").groups.add(europa)
    Territory.objects.create(
        code="fo", wikipedia_link="https://en.wikipedia.org/wiki/Faroe_Islands").groups.add(europa)
    Territory.objects.create(
        code="se", wikipedia_link="https://en.wikipedia.org/wiki/Sweden").groups.add(europa)
    Territory.objects.create(
        code="pt", wikipedia_link="https://en.wikipedia.org/wiki/Portugal").groups.add(europa)
    Territory.objects.create(
        code="ua", wikipedia_link="https://en.wikipedia.org/wiki/Ukraine").groups.add(europa)
    Territory.objects.create(
        code="fi", wikipedia_link="https://en.wikipedia.org/wiki/Finland").groups.add(europa)
    Territory.objects.create(
        code="sm", wikipedia_link="https://en.wikipedia.org/wiki/San_Marino").groups.add(europa)
    Territory.objects.create(
        code="hu", wikipedia_link="https://en.wikipedia.org/wiki/Hungary").groups.add(europa)
    Territory.objects.create(
        code="je", wikipedia_link="https://en.wikipedia.org/wiki/Jersey").groups.add(europa)
    Territory.objects.create(
        code="gi", wikipedia_link="https://en.wikipedia.org/wiki/Gibraltar").groups.add(europa)
    Territory.objects.create(
        code="me", wikipedia_link="https://en.wikipedia.org/wiki/Montenegro").groups.add(europa)
    Territory.objects.create(
        code="lv", wikipedia_link="https://en.wikipedia.org/wiki/Latvia").groups.add(europa)
    Territory.objects.create(
        code="ad", wikipedia_link="https://en.wikipedia.org/wiki/Andorra").groups.add(europa)
    Territory.objects.create(
        code="it", wikipedia_link="https://en.wikipedia.org/wiki/Italy").groups.add(europa)
    Territory.objects.create(
        code="mt", wikipedia_link="https://en.wikipedia.org/wiki/Malta").groups.add(europa)
    Territory.objects.create(
        code="ro", wikipedia_link="https://en.wikipedia.org/wiki/Romania").groups.add(europa)
    Territory.objects.create(
        code="gg", wikipedia_link="https://en.wikipedia.org/wiki/Guernsey").groups.add(europa)
    Territory.objects.create(
        code="ax", wikipedia_link="https://en.wikipedia.org/wiki/%C3%85land_Islands").groups.add(europa)
    Territory.objects.create(
        code="is", wikipedia_link="https://en.wikipedia.org/wiki/Iceland").groups.add(europa)
    Territory.objects.create(
        code="md", wikipedia_link="https://en.wikipedia.org/wiki/Moldova").groups.add(europa)
    Territory.objects.create(
        code="de", wikipedia_link="https://en.wikipedia.org/wiki/Germany").groups.add(europa)
    Territory.objects.create(
        code="ch", wikipedia_link="https://en.wikipedia.org/wiki/Switzerland").groups.add(europa)
    Territory.objects.create(
        code="by", wikipedia_link="https://en.wikipedia.org/wiki/Belarus").groups.add(europa)
    Territory.objects.create(
        code="mk", wikipedia_link="https://en.wikipedia.org/wiki/North_Macedonia").groups.add(europa)
    Territory.objects.create(
        code="sj", wikipedia_link="https://en.wikipedia.org/wiki/Svalbard_and_Jan_Mayen").groups.add(europa)
    Territory.objects.create(
        code="bg", wikipedia_link="https://en.wikipedia.org/wiki/Bulgaria").groups.add(europa)
    Territory.objects.create(
        code="gb", wikipedia_link="https://en.wikipedia.org/wiki/United_Kingdom").groups.add(europa)

    #  ▄██████▄   ▄████████    ▄████████    ▄████████ ███▄▄▄▄    ▄█     ▄████████
    # ███    ███ ███    ███   ███    ███   ███    ███ ███▀▀▀██▄ ███    ███    ███
    # ███    ███ ███    █▀    ███    █▀    ███    ███ ███   ███ ███▌   ███    ███
    # ███    ███ ███         ▄███▄▄▄       ███    ███ ███   ███ ███▌   ███    ███
    # ███    ███ ███        ▀▀███▀▀▀     ▀███████████ ███   ███ ███▌ ▀███████████
    # ███    ███ ███    █▄    ███    █▄    ███    ███ ███   ███ ███    ███    ███
    # ███    ███ ███    ███   ███    ███   ███    ███ ███   ███ ███    ███    ███
    #  ▀██████▀  ████████▀    ██████████   ███    █▀   ▀█   █▀  █▀     ███    █▀

    Territory.objects.create(
        code="hm", wikipedia_link="https://en.wikipedia.org/wiki/Heard_Island_and_McDonald_Islands").groups.add(oceania)
    Territory.objects.create(
        code="nu", wikipedia_link="https://en.wikipedia.org/wiki/Niue").groups.add(oceania)
    Territory.objects.create(
        code="pn", wikipedia_link="https://en.wikipedia.org/wiki/Pitcairn_Islands").groups.add(oceania)
    Territory.objects.create(
        code="um", wikipedia_link="https://en.wikipedia.org/wiki/United_States_Minor_Outlying_Islands").groups.add(oceania)
    Territory.objects.create(
        code="tk", wikipedia_link="https://en.wikipedia.org/wiki/Tokelau").groups.add(oceania)
    Territory.objects.create(
        code="gs", wikipedia_link="https://en.wikipedia.org/wiki/South_Georgia_and_the_South_Sandwich_Islands").groups.add(oceania)
    Territory.objects.create(
        code="mp", wikipedia_link="https://en.wikipedia.org/wiki/Northern_Mariana_Islands").groups.add(oceania)
    Territory.objects.create(
        code="pw", wikipedia_link="https://en.wikipedia.org/wiki/Palau").groups.add(oceania)
    Territory.objects.create(
        code="mh", wikipedia_link="https://en.wikipedia.org/wiki/Marshall_Islands").groups.add(oceania)
    Territory.objects.create(
        code="nz", wikipedia_link="https://en.wikipedia.org/wiki/New_Zealand").groups.add(oceania)
    Territory.objects.create(
        code="fm", wikipedia_link="https://en.wikipedia.org/wiki/Micronesia").groups.add(oceania)
    Territory.objects.create(
        code="nc", wikipedia_link="https://en.wikipedia.org/wiki/New_Caledonia").groups.add(oceania)
    Territory.objects.create(
        code="fj", wikipedia_link="https://en.wikipedia.org/wiki/Fiji").groups.add(oceania)
    Territory.objects.create(
        code="as", wikipedia_link="https://en.wikipedia.org/wiki/American_Samoa").groups.add(oceania)
    Territory.objects.create(
        code="pf", wikipedia_link="https://en.wikipedia.org/wiki/French_Polynesia").groups.add(oceania)
    Territory.objects.create(
        code="to", wikipedia_link="https://en.wikipedia.org/wiki/Tonga").groups.add(oceania)
    Territory.objects.create(
        code="nr", wikipedia_link="https://en.wikipedia.org/wiki/Nauru").groups.add(oceania)
    Territory.objects.create(
        code="vu", wikipedia_link="https://en.wikipedia.org/wiki/Vanuatu").groups.add(oceania)
    Territory.objects.create(
        code="pg", wikipedia_link="https://en.wikipedia.org/wiki/Papua_New_Guinea").groups.add(oceania)
    Territory.objects.create(
        code="nf", wikipedia_link="https://en.wikipedia.org/wiki/Norfolk_Island").groups.add(oceania)
    Territory.objects.create(
        code="au", wikipedia_link="https://en.wikipedia.org/wiki/Australia").groups.add(oceania)
    Territory.objects.create(
        code="cx", wikipedia_link="https://en.wikipedia.org/wiki/Christmas_Island").groups.add(oceania)
    Territory.objects.create(
        code="wf", wikipedia_link="https://en.wikipedia.org/wiki/Wallis_and_Futuna").groups.add(oceania)
    Territory.objects.create(
        code="ki", wikipedia_link="https://en.wikipedia.org/wiki/Kiribati").groups.add(oceania)
    Territory.objects.create(
        code="ws", wikipedia_link="https://en.wikipedia.org/wiki/Samoa").groups.add(oceania)
    Territory.objects.create(
        code="gu", wikipedia_link="https://en.wikipedia.org/wiki/Guam").groups.add(oceania)
    Territory.objects.create(
        code="ck", wikipedia_link="https://en.wikipedia.org/wiki/Cook_Islands").groups.add(oceania)
    Territory.objects.create(
        code="sb", wikipedia_link="https://en.wikipedia.org/wiki/Solomon_Islands").groups.add(oceania)
    Territory.objects.create(
        code="tv", wikipedia_link="https://en.wikipedia.org/wiki/Tuvalu").groups.add(oceania)

    #    ▄████████    ▄████████    ▄████████  ▄█   ▄████████    ▄████████
    #   ███    ███   ███    ███   ███    ███ ███  ███    ███   ███    ███
    #   ███    ███   ███    █▀    ███    ███ ███▌ ███    █▀    ███    ███
    #   ███    ███  ▄███▄▄▄      ▄███▄▄▄▄██▀ ███▌ ███          ███    ███
    # ▀███████████ ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   ███▌ ███        ▀███████████
    #   ███    ███   ███        ▀███████████ ███  ███    █▄    ███    ███
    #   ███    ███   ███          ███    ███ ███  ███    ███   ███    ███
    #   ███    █▀    ███          ███    ███ █▀   ████████▀    ███    █▀
    #                             ███    ███

    Territory.objects.create(
        code="bw", wikipedia_link="https://en.wikipedia.org/wiki/Botswana").groups.add(africa)
    Territory.objects.create(
        code="zm", wikipedia_link="https://en.wikipedia.org/wiki/Zambia").groups.add(africa)
    Territory.objects.create(
        code="km", wikipedia_link="https://en.wikipedia.org/wiki/Comoros").groups.add(africa)
    Territory.objects.create(
        code="gh", wikipedia_link="https://en.wikipedia.org/wiki/Ghana").groups.add(africa)
    Territory.objects.create(
        code="eh", wikipedia_link="https://en.wikipedia.org/wiki/Western_Sahara").groups.add(africa)
    Territory.objects.create(
        code="ga", wikipedia_link="https://en.wikipedia.org/wiki/Gabon").groups.add(africa)
    Territory.objects.create(
        code="sc", wikipedia_link="https://en.wikipedia.org/wiki/Seychelles").groups.add(africa)
    Territory.objects.create(
        code="zw", wikipedia_link="https://en.wikipedia.org/wiki/Zimbabwe").groups.add(africa)
    Territory.objects.create(
        code="lr", wikipedia_link="https://en.wikipedia.org/wiki/Liberia").groups.add(africa)
    Territory.objects.create(
        code="ci", wikipedia_link="https://en.wikipedia.org/wiki/Ivory_Coast").groups.add(africa)
    Territory.objects.create(
        code="sn", wikipedia_link="https://en.wikipedia.org/wiki/Senegal").groups.add(africa)
    Territory.objects.create(
        code="dj", wikipedia_link="https://en.wikipedia.org/wiki/Djibouti").groups.add(africa)
    Territory.objects.create(
        code="ao", wikipedia_link="https://en.wikipedia.org/wiki/Angola").groups.add(africa)
    Territory.objects.create(
        code="ss", wikipedia_link="https://en.wikipedia.org/wiki/South_Sudan").groups.add(africa)
    Territory.objects.create(
        code="gm", wikipedia_link="https://en.wikipedia.org/wiki/Gambia").groups.add(africa)
    Territory.objects.create(
        code="ng", wikipedia_link="https://en.wikipedia.org/wiki/Nigeria").groups.add(africa)
    Territory.objects.create(
        code="gw", wikipedia_link="https://en.wikipedia.org/wiki/Guinea-Bissau").groups.add(africa)
    Territory.objects.create(
        code="za", wikipedia_link="https://en.wikipedia.org/wiki/South_Africa").groups.add(africa)
    Territory.objects.create(
        code="ne", wikipedia_link="https://en.wikipedia.org/wiki/Niger").groups.add(africa)
    Territory.objects.create(
        code="gn", wikipedia_link="https://en.wikipedia.org/wiki/Guinea").groups.add(africa)
    Territory.objects.create(
        code="ma", wikipedia_link="https://en.wikipedia.org/wiki/Morocco").groups.add(africa)
    Territory.objects.create(
        code="yt", wikipedia_link="https://en.wikipedia.org/wiki/Mayotte").groups.add(africa)
    Territory.objects.create(
        code="mu", wikipedia_link="https://en.wikipedia.org/wiki/Mauritius").groups.add(africa)
    Territory.objects.create(
        code="et", wikipedia_link="https://en.wikipedia.org/wiki/Ethiopia").groups.add(africa)
    Territory.objects.create(
        code="rw", wikipedia_link="https://en.wikipedia.org/wiki/Rwanda").groups.add(africa)
    Territory.objects.create(
        code="cg", wikipedia_link="https://en.wikipedia.org/wiki/Republic_of_the_Congo").groups.add(africa)
    Territory.objects.create(
        code="cf", wikipedia_link="https://en.wikipedia.org/wiki/Central_African_Republic").groups.add(africa)
    Territory.objects.create(
        code="na", wikipedia_link="https://en.wikipedia.org/wiki/Namibia").groups.add(africa)
    Territory.objects.create(
        code="cv", wikipedia_link="https://en.wikipedia.org/wiki/Cape_Verde").groups.add(africa)
    Territory.objects.create(
        code="sh", wikipedia_link="https://en.wikipedia.org/wiki/Saint_Helena").groups.add(africa)
    Territory.objects.create(
        code="tn", wikipedia_link="https://en.wikipedia.org/wiki/Tunisia").groups.add(africa)
    Territory.objects.create(
        code="mw", wikipedia_link="https://en.wikipedia.org/wiki/Malawi").groups.add(africa)
    Territory.objects.create(
        code="re", wikipedia_link="https://en.wikipedia.org/wiki/R%C3%A9union").groups.add(africa)
    Territory.objects.create(
        code="bf", wikipedia_link="https://en.wikipedia.org/wiki/Burkina_Faso").groups.add(africa)
    Territory.objects.create(
        code="sz", wikipedia_link="https://en.wikipedia.org/wiki/Swaziland").groups.add(africa)
    Territory.objects.create(
        code="mg", wikipedia_link="https://en.wikipedia.org/wiki/Madagascar").groups.add(africa)
    Territory.objects.create(
        code="mz", wikipedia_link="https://en.wikipedia.org/wiki/Mozambique").groups.add(africa)
    Territory.objects.create(
        code="sd", wikipedia_link="https://en.wikipedia.org/wiki/Sudan").groups.add(africa)
    Territory.objects.create(
        code="cm", wikipedia_link="https://en.wikipedia.org/wiki/Cameroon").groups.add(africa)
    Territory.objects.create(
        code="bi", wikipedia_link="https://en.wikipedia.org/wiki/Burundi").groups.add(africa)
    Territory.objects.create(
        code="so", wikipedia_link="https://en.wikipedia.org/wiki/Somalia").groups.add(africa)
    Territory.objects.create(
        code="bj", wikipedia_link="https://en.wikipedia.org/wiki/Benin").groups.add(africa)
    Territory.objects.create(
        code="tg", wikipedia_link="https://en.wikipedia.org/wiki/Togo").groups.add(africa)
    Territory.objects.create(
        code="td", wikipedia_link="https://en.wikipedia.org/wiki/Chad").groups.add(africa)
    Territory.objects.create(
        code="gq", wikipedia_link="https://en.wikipedia.org/wiki/Equatorial_Guinea").groups.add(africa)
    Territory.objects.create(
        code="cd", wikipedia_link="https://en.wikipedia.org/wiki/Democratic_Republic_of_the_Congo").groups.add(africa)
    Territory.objects.create(
        code="eg", wikipedia_link="https://en.wikipedia.org/wiki/Egypt").groups.add(africa)
    Territory.objects.create(
        code="er", wikipedia_link="https://en.wikipedia.org/wiki/Eritrea").groups.add(africa)
    Territory.objects.create(
        code="st", wikipedia_link="https://en.wikipedia.org/wiki/Sao_Tome_and_Principe").groups.add(africa)
    Territory.objects.create(
        code="ke", wikipedia_link="https://en.wikipedia.org/wiki/Kenya").groups.add(africa)
    Territory.objects.create(
        code="tz", wikipedia_link="https://en.wikipedia.org/wiki/Tanzania").groups.add(africa)
    Territory.objects.create(
        code="ug", wikipedia_link="https://en.wikipedia.org/wiki/Uganda").groups.add(africa)
    Territory.objects.create(
        code="sl", wikipedia_link="https://en.wikipedia.org/wiki/Sierra_Leone").groups.add(africa)
    Territory.objects.create(
        code="dz", wikipedia_link="https://en.wikipedia.org/wiki/Algeria").groups.add(africa)
    Territory.objects.create(
        code="ly", wikipedia_link="https://en.wikipedia.org/wiki/Libya").groups.add(africa)
    Territory.objects.create(
        code="ml", wikipedia_link="https://en.wikipedia.org/wiki/Mali").groups.add(africa)
    Territory.objects.create(
        code="mr", wikipedia_link="https://en.wikipedia.org/wiki/Mauritania").groups.add(africa)
    Territory.objects.create(
        code="ls", wikipedia_link="https://en.wikipedia.org/wiki/Lesotho").groups.add(africa)

    # ███▄▄▄▄    ▄██████▄     ▄████████     ███        ▄█    █▄            ▄████████   ▄▄▄▄███▄▄▄▄      ▄████████    ▄████████  ▄█   ▄████████    ▄████████
    # ███▀▀▀██▄ ███    ███   ███    ███ ▀█████████▄   ███    ███          ███    ███ ▄██▀▀▀███▀▀▀██▄   ███    ███   ███    ███ ███  ███    ███   ███    ███
    # ███   ███ ███    ███   ███    ███    ▀███▀▀██   ███    ███          ███    ███ ███   ███   ███   ███    █▀    ███    ███ ███▌ ███    █▀    ███    ███
    # ███   ███ ███    ███  ▄███▄▄▄▄██▀     ███   ▀  ▄███▄▄▄▄███▄▄        ███    ███ ███   ███   ███  ▄███▄▄▄      ▄███▄▄▄▄██▀ ███▌ ███          ███    ███
    # ███   ███ ███    ███ ▀▀███▀▀▀▀▀       ███     ▀▀███▀▀▀▀███▀       ▀███████████ ███   ███   ███ ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   ███▌ ███        ▀███████████
    # ███   ███ ███    ███ ▀███████████     ███       ███    ███          ███    ███ ███   ███   ███   ███    █▄  ▀███████████ ███  ███    █▄    ███    ███
    # ███   ███ ███    ███   ███    ███     ███       ███    ███          ███    ███ ███   ███   ███   ███    ███   ███    ███ ███  ███    ███   ███    ███
    #  ▀█   █▀   ▀██████▀    ███    ███    ▄████▀     ███    █▀           ███    █▀   ▀█   ███   █▀    ██████████   ███    ███ █▀   ████████▀    ███    █▀
    #                        ███    ███                                                                             ███    ███

    Territory.objects.create(
        code="bq", wikipedia_link="https://en.wikipedia.org/wiki/Bonaire,_Sint_Eustatius_and_Saba").groups.add(north_america)
    Territory.objects.create(
        code="mf", wikipedia_link="https://en.wikipedia.org/wiki/Saint_Martin").groups.add(north_america)
    Territory.objects.create(
        code="ai", wikipedia_link="https://en.wikipedia.org/wiki/Anguilla").groups.add(north_america)
    Territory.objects.create(
        code="bl", wikipedia_link="https://en.wikipedia.org/wiki/Saint_Barth%C3%A9lemy").groups.add(north_america)
    Territory.objects.create(
        code="ms", wikipedia_link="https://en.wikipedia.org/wiki/Montserrat").groups.add(north_america)
    Territory.objects.create(
        code="gp", wikipedia_link="https://en.wikipedia.org/wiki/Guadeloupe").groups.add(north_america)
    Territory.objects.create(
        code="us", wikipedia_link="https://en.wikipedia.org/wiki/United_States").groups.add(north_america)
    Territory.objects.create(
        code="dm", wikipedia_link="https://en.wikipedia.org/wiki/Dominica").groups.add(north_america)
    Territory.objects.create(
        code="cu", wikipedia_link="https://en.wikipedia.org/wiki/Cuba").groups.add(north_america)
    Territory.objects.create(
        code="ni", wikipedia_link="https://en.wikipedia.org/wiki/Nicaragua").groups.add(north_america)
    Territory.objects.create(
        code="vi", wikipedia_link="https://en.wikipedia.org/wiki/United_States_Virgin_Islands").groups.add(north_america)
    Territory.objects.create(
        code="cr", wikipedia_link="https://en.wikipedia.org/wiki/Costa_Rica").groups.add(north_america)
    Territory.objects.create(
        code="vc", wikipedia_link="https://en.wikipedia.org/wiki/Saint_Vincent_and_the_Grenadines").groups.add(north_america)
    Territory.objects.create(
        code="aw", wikipedia_link="https://en.wikipedia.org/wiki/Aruba").groups.add(north_america)
    Territory.objects.create(
        code="ky", wikipedia_link="https://en.wikipedia.org/wiki/Cayman_Islands").groups.add(north_america)
    Territory.objects.create(
        code="mx", wikipedia_link="https://en.wikipedia.org/wiki/Mexico").groups.add(north_america)
    Territory.objects.create(
        code="jm", wikipedia_link="https://en.wikipedia.org/wiki/Jamaica").groups.add(north_america)
    Territory.objects.create(
        code="gd", wikipedia_link="https://en.wikipedia.org/wiki/Grenada").groups.add(north_america)
    Territory.objects.create(
        code="mq", wikipedia_link="https://en.wikipedia.org/wiki/Martinique").groups.add(north_america)
    Territory.objects.create(
        code="tt", wikipedia_link="https://en.wikipedia.org/wiki/Trinidad_and_Tobago").groups.add(north_america)
    Territory.objects.create(
        code="cw", wikipedia_link="https://en.wikipedia.org/wiki/Cura%C3%A7ao").groups.add(north_america)
    Territory.objects.create(
        code="gl", wikipedia_link="https://en.wikipedia.org/wiki/Greenland").groups.add(north_america)
    Territory.objects.create(
        code="pm", wikipedia_link="https://en.wikipedia.org/wiki/Saint_Pierre_and_Miquelon").groups.add(north_america)
    Territory.objects.create(
        code="do", wikipedia_link="https://en.wikipedia.org/wiki/Dominican_Republic").groups.add(north_america)
    Territory.objects.create(
        code="pr", wikipedia_link="https://en.wikipedia.org/wiki/Puerto_Rico").groups.add(north_america)
    Territory.objects.create(
        code="ag", wikipedia_link="https://en.wikipedia.org/wiki/Antigua_and_Barbuda").groups.add(north_america)
    Territory.objects.create(
        code="hn", wikipedia_link="https://en.wikipedia.org/wiki/Honduras").groups.add(north_america)
    Territory.objects.create(
        code="ca", wikipedia_link="https://en.wikipedia.org/wiki/Canada").groups.add(north_america)
    Territory.objects.create(
        code="bm", wikipedia_link="https://en.wikipedia.org/wiki/Bermuda").groups.add(north_america)
    Territory.objects.create(
        code="ht", wikipedia_link="https://en.wikipedia.org/wiki/Haiti").groups.add(north_america)
    Territory.objects.create(
        code="kn", wikipedia_link="https://en.wikipedia.org/wiki/Saint_Kitts_and_Nevis").groups.add(north_america)
    Territory.objects.create(
        code="bb", wikipedia_link="https://en.wikipedia.org/wiki/Barbados").groups.add(north_america)
    Territory.objects.create(
        code="lc", wikipedia_link="https://en.wikipedia.org/wiki/Saint_Lucia").groups.add(north_america)
    Territory.objects.create(
        code="bz", wikipedia_link="https://en.wikipedia.org/wiki/Belize").groups.add(north_america)
    Territory.objects.create(
        code="sx", wikipedia_link="https://en.wikipedia.org/wiki/Sint_Maarten").groups.add(north_america)
    Territory.objects.create(
        code="gt", wikipedia_link="https://en.wikipedia.org/wiki/Guatemala").groups.add(north_america)
    Territory.objects.create(
        code="pa", wikipedia_link="https://en.wikipedia.org/wiki/Panama").groups.add(north_america)
    Territory.objects.create(
        code="vg", wikipedia_link="https://en.wikipedia.org/wiki/British_Virgin_Islands").groups.add(north_america)
    Territory.objects.create(
        code="bs", wikipedia_link="https://en.wikipedia.org/wiki/Bahamas").groups.add(north_america)
    Territory.objects.create(
        code="tc", wikipedia_link="https://en.wikipedia.org/wiki/Turks_and_Caicos_Islands").groups.add(north_america)
    Territory.objects.create(
        code="sv", wikipedia_link="https://en.wikipedia.org/wiki/El_Salvador").groups.add(north_america)

    #    ▄████████  ▄██████▄  ███    █▄      ███        ▄█    █▄            ▄████████   ▄▄▄▄███▄▄▄▄      ▄████████    ▄████████  ▄█   ▄████████    ▄████████
    #   ███    ███ ███    ███ ███    ███ ▀█████████▄   ███    ███          ███    ███ ▄██▀▀▀███▀▀▀██▄   ███    ███   ███    ███ ███  ███    ███   ███    ███
    #   ███    █▀  ███    ███ ███    ███    ▀███▀▀██   ███    ███          ███    ███ ███   ███   ███   ███    █▀    ███    ███ ███▌ ███    █▀    ███    ███
    #   ███        ███    ███ ███    ███     ███   ▀  ▄███▄▄▄▄███▄▄        ███    ███ ███   ███   ███  ▄███▄▄▄      ▄███▄▄▄▄██▀ ███▌ ███          ███    ███
    # ▀███████████ ███    ███ ███    ███     ███     ▀▀███▀▀▀▀███▀       ▀███████████ ███   ███   ███ ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   ███▌ ███        ▀███████████
    #          ███ ███    ███ ███    ███     ███       ███    ███          ███    ███ ███   ███   ███   ███    █▄  ▀███████████ ███  ███    █▄    ███    ███
    #    ▄█    ███ ███    ███ ███    ███     ███       ███    ███          ███    ███ ███   ███   ███   ███    ███   ███    ███ ███  ███    ███   ███    ███
    #  ▄████████▀   ▀██████▀  ████████▀     ▄████▀     ███    █▀           ███    █▀   ▀█   ███   █▀    ██████████   ███    ███ █▀   ████████▀    ███    █▀
    #                                                                                                                ███    ███

    Territory.objects.create(
        code="fk", wikipedia_link="https://en.wikipedia.org/wiki/Falkland_Islands").groups.add(south_america)
    Territory.objects.create(
        code="ve", wikipedia_link="https://en.wikipedia.org/wiki/Venezuela").groups.add(south_america)
    Territory.objects.create(
        code="gf", wikipedia_link="https://en.wikipedia.org/wiki/French_Guiana").groups.add(south_america)
    Territory.objects.create(
        code="ec", wikipedia_link="https://en.wikipedia.org/wiki/Ecuador").groups.add(south_america)
    Territory.objects.create(
        code="bo", wikipedia_link="https://en.wikipedia.org/wiki/Bolivia").groups.add(south_america)
    Territory.objects.create(
        code="pe", wikipedia_link="https://en.wikipedia.org/wiki/Peru").groups.add(south_america)
    Territory.objects.create(
        code="gy", wikipedia_link="https://en.wikipedia.org/wiki/Guyana").groups.add(south_america)
    Territory.objects.create(
        code="co", wikipedia_link="https://en.wikipedia.org/wiki/Colombia").groups.add(south_america)
    Territory.objects.create(
        code="br", wikipedia_link="https://en.wikipedia.org/wiki/Brazil").groups.add(south_america)
    Territory.objects.create(
        code="ar", wikipedia_link="https://en.wikipedia.org/wiki/Argentina").groups.add(south_america)
    Territory.objects.create(
        code="cl", wikipedia_link="https://en.wikipedia.org/wiki/Chile").groups.add(south_america)
    Territory.objects.create(
        code="uy", wikipedia_link="https://en.wikipedia.org/wiki/Uruguay").groups.add(south_america)
    Territory.objects.create(
        code="sr", wikipedia_link="https://en.wikipedia.org/wiki/Suriname").groups.add(south_america)
    Territory.objects.create(
        code="py", wikipedia_link="https://en.wikipedia.org/wiki/Paraguay").groups.add(south_america)

    #    ▄████████ ███▄▄▄▄       ███        ▄████████    ▄████████  ▄████████     ███      ▄█   ▄████████    ▄████████
    #   ███    ███ ███▀▀▀██▄ ▀█████████▄   ███    ███   ███    ███ ███    ███ ▀█████████▄ ███  ███    ███   ███    ███
    #   ███    ███ ███   ███    ▀███▀▀██   ███    ███   ███    ███ ███    █▀     ▀███▀▀██ ███▌ ███    █▀    ███    ███
    #   ███    ███ ███   ███     ███   ▀   ███    ███  ▄███▄▄▄▄██▀ ███            ███   ▀ ███▌ ███          ███    ███
    # ▀███████████ ███   ███     ███     ▀███████████ ▀▀███▀▀▀▀▀   ███            ███     ███▌ ███        ▀███████████
    #   ███    ███ ███   ███     ███       ███    ███ ▀███████████ ███    █▄      ███     ███  ███    █▄    ███    ███
    #   ███    ███ ███   ███     ███       ███    ███   ███    ███ ███    ███     ███     ███  ███    ███   ███    ███
    #   ███    █▀   ▀█   █▀     ▄████▀     ███    █▀    ███    ███ ████████▀     ▄████▀   █▀   ████████▀    ███    █▀
    #                                                   ███    ███

    Territory.objects.create(
        code="bv", wikipedia_link="https://en.wikipedia.org/wiki/Bouvet_Island").groups.add(antarctica)
    Territory.objects.create(
        code="tf", wikipedia_link="https://en.wikipedia.org/wiki/French_Southern_and_Antarctic_Lands").groups.add(antarctica)

    # Import Country names

    for language in Language.objects.all():
        code = language.code
        with open("./script/%s_names.json" % code, "r") as f:
            json_data = json.load(f)
            for territory_code, name in json_data.items():
                if Territory.objects.filter(code=territory_code).exists():
                    TerritoryName.objects.create(territory=Territory.objects.get(
                        code=territory_code), language=language, name=name)


main()
