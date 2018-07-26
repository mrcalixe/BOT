import googlemaps, requests, json


send_url = 'http://freegeoip.net/json'
r = requests.get(send_url)
j = json.loads(r.text)
lat = '41.550031'
lon = '-8.422311'
geo_loc = (lat, lon)
language = 'pt-PT'

api_places_key = "AIzaSyC-RUQ7A1Iu8Hvup-J8h22B3JCvgNwjZdc"

gmaps = googlemaps.Client(key=api_places_key)


Resultado_exemplo = {'status': 'OK',
             'html_attributions': [],
             'results': [{'opening_hours': {'open_now': True,
                                            'weekday_text': []},
                          'id': '75a5ca8f6292742784a6554d25ef4419bd7082cd',
                          'types': ['bar', 'restaurant', 'food', 'point_of_interest', 'establishment'],
                          'name': 'Taberna Real Restaurante',
                          'formatted_address': 'Plaza de Isabel II, 8, 28013 Madrid, Spain',
                          'place_id': 'ChIJyb9X4HsoQg0R6H4IOS4TWoQ',
                          'geometry': {'viewport': {'northeast': {'lng': -3.707699570107278, 'lat': 40.41930217989273},
                                                    'southwest': {'lng': -3.710399229892722, 'lat': 40.41660252010729}},
                                       'location': {'lng': -3.7089828, 'lat': 40.4179453}},
                          'rating': 3.3,
                          'photos': [{'height': 3024, 'width': 4032,
                                      'html_attributions': ['<a href="https://maps.google.com/maps/contrib/107583755559978253636/photos">A Google User</a>'],
                                      'photo_reference': 'CmRaAAAATwsuxlK9aLpYt1N8MjdupNxMmb5ttvGKlnFHHUaN3DVxOpCcqRteNTp91oGyOdvByOVLHCGEa3K5XLL8ct48TDKnKJAWTBaqNlM9P29wn_q_nb4r6RkRp0NcMn-maQymEhDkUfCzFPkiwV9dmIWy2MvpGhTHdPVIZU3wxvDQEX0sPlaumzx47g'}],
                          'reference': 'CmRbAAAAh_Cx2X2xyntD3_X2ynqlTNZmWPOY_-NV8FMFc5j0Fa8q7qe0SAkcmz16N-yXkAmi8vK4eudrlBDV4QuyVVfTnUJc4KRs3AS-pzaNWFvWbICwp6UIbZmBnWJVb1IIJDyXEhA23q6xCu5p-119AOG8Xxt3GhR-uNSHQBru2g2AacotiYBRHkxh5g',
                          'icon': 'https://maps.gstatic.com/mapfiles/place_api/icons/restaurant-71.png'},
                         {'opening_hours': {'open_now': False, 'weekday_text': []},
                          'id': '5704426aff31a9ffd715f0ea12e5730adffa8792',
                          'types': ['restaurant', 'food', 'point_of_interest', 'establishment'],
                          'name': 'Real Taberna',
                          'formatted_address': 'R. Costa Gomes 497, 4700-260 Real, Portugal',
                          'place_id': 'ChIJX8zqVhv_JA0RJpF_YRFY7As',
                          'geometry': {'viewport': {'northeast': {'lng': -8.444686520107277, 'lat': 41.56068442989271},
                                                    'southwest': {'lng': -8.447386179892721, 'lat': 41.55798477010727}},
                                       'location': {'lng': -8.4460448, 'lat': 41.55932749999999}},
                          'rating': 4.4,
                          'photos': [{'height': 1080, 'width': 1920, 'html_attributions': ['<a href="https://maps.google.com/maps/contrib/116809869330923555182/photos">A Google User</a>'], 'photo_reference': 'CmRaAAAArhFTLKcI3N-8qXtQzHlii87jrtMeGbvqQdtKazEqr7BOKtCDqajnjC2zg90F3Ka26t5AfaGZmWtHo-uZypCoo71qYkCgwVOMBnjEZ0jm5-76C8NVe84hT_nYrb9AwXnNEhDfM4zBzBZbJ7fzlHtVZWEIGhT5SnvkAM85NySyM_qsFUx-rlgGfw'}],
                          'reference': 'CmRbAAAAHM1vwVk3Bcr-CHW2zIZRwUsI9qrHcbtysF6feH_ZfExar-GmPXs4flZwIntgDoGMZIfTGjsQiOT2nqu2UxC1GfKLQRl4-SI2uxWIy9nD81ocSA7l0YsYwX_lW10q3pxaEhDH7CA1hWGjtw2XJ-YH7RbrGhQFMifITWvCaxVD0A6CH-eKT3VHqQ',
                          'icon': 'https://maps.gstatic.com/mapfiles/place_api/icons/restaurant-71.png'}]}


def escolhe_opcao(resultado):
    opcoes = []
    i = 1
    print('Encontrei mais do que 1 resultado...')
    for place in resultado:
        print(str(i) + ' - ' + place['name'] + ' em ' + place['formatted_address'] + ';')
        opcoes.insert(i-1, place)
        i += 1
    op = int(input('Qual deles é que quer escolher: '))
    while op < 1 and op > (len(opcoes)+1):
        op = input('Opção errada...\nTente novamente: ')
    return opcoes[op-1]

def procura_lugar(lugar):
    print("DEBUG:GMAPS:input", lugar)
    global gmaps, geo_loc, language
    resultado = gmaps.places(lugar, location=geo_loc, language=language)
    if len(resultado['results']) > 1:
        # Imprimir os que encontrou
        res = escolhe_opcao(resultado['results'])
    elif len(resultado['results']) == 1:
        res = resultado['results'][0]
    else:
        return None

    return res['name'] + ' situa-se em ' + res['formatted_address']#, res['types']#, res['rating']


#places('restaurant', location=self.location,
 #                          radius=self.radius, language=self.language,
  #                         min_price=1, max_price=4, open_now=True,
   #                        type=self.type)