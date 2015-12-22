# coding=utf-8
import requests

print 'test'
indexfile='''
<!DOCTYPE HTML>
<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
		<title>İnceleme Bekleyen Değişilikler</title>

		<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js"></script>
		<script src="https://code.highcharts.com/highcharts.js"></script>
		<!-- <script src="https://code.highcharts.com/modules/exporting.js"></script> -->

		<style type="text/css">
			${demo.css}
		</style>
		<script type="text/javascript">
			$(function () {
				Highcharts.setOptions({
					global: {
						useUTC: false
					},
					lang: {
						months: ['Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs', 'Haziran',  'Temmuz', 'Ağustos', 'Eylül', 'Ekim', 'Kasım', 'Aralık'],
						weekdays: [ 'Pazar', 'Pazartesi', 'Salı', 'Çarşamba', 'Perşembe', 'Cuma', 'Cumartesi'],
						shortMonths: [ 'Oca', 'Şub', 'Mar', 'Nis', 'May', 'Haz', 'Tem', 'Ağu', 'Eyl', 'Eki', 'Kas', 'Ara'],
						resetZoom : 'Sıfırla'
					}
				});
				$('#container').highcharts({
					chart: {
						type: 'spline',
						zoomType: 'xy'
					},
					title: {
						text: 'İnceleme Bekleyen Değişilikler'
					},
					subtitle: {
						text: 'Türkçe Vikipedi, UTC'
					},
					xAxis: {
						type: 'datetime',
						dateTimeLabelFormats: { // don't display the dummy year
							month: '%e. %b',
							year: '%b'
						},
						title: {
							text: 'Zaman'
						}
					},
					yAxis: {
						title: {
							text: 'Madde sayısı'
						},
						//min: 0
					},
					credits: {
						enabled: true,
						href: 'https://tr.wikipedia.org/wiki/%C3%96zel:Do%C4%9Frulama%C4%B0statistikleri',
						text: 'Özel:Doğrulama İstatistikleri'
					},
					plotOptions: {
						spline: {
							marker: {
								enabled: false
							}
						}
					},

					series: [{
						name: 'Güncelliğini yitirmiş/Madde',
						data: [
[Date.parse('12/20/2014 01:54:00'), 4300],
[Date.parse('12/20/2014 17:49:00'), 4100],
[Date.parse('12/21/2014 20:24:00'), 4048],
[Date.parse('12/21/2014 22:12:00'), 4070],
[Date.parse('12/22/2014 00:24:00'), 4073],
[Date.parse('12/22/2014 12:17:00'), 4043],
[Date.parse('12/22/2014 14:23:00'), 4020],
[Date.parse('12/22/2014 16:17:00'), 4030],
[Date.parse('12/22/2014 18:20:00'), 4042],
[Date.parse('12/22/2014 20:24:00'), 4070],
[Date.parse('12/22/2014 22:23:00'), 3747],
[Date.parse('12/23/2014 00:15:00'), 3732],
[Date.parse('12/23/2014 02:19:00'), 3723],
[Date.parse('12/23/2014 04:09:00'), 3725],
[Date.parse('12/23/2014 06:17:00'), 3698],
[Date.parse('12/23/2014 08:12:00'), 3677],
[Date.parse('12/23/2014 10:10:00'), 3638],
[Date.parse('12/23/2014 12:26:00'), 3676],
[Date.parse('12/23/2014 18:25:00'), 3736],
[Date.parse('12/23/2014 20:20:00'), 3711],
[Date.parse('12/23/2014 21:56:00'), 3742],
[Date.parse('12/23/2014 22:14:00'), 3747],
[Date.parse('12/24/2014 00:13:00'), 3746],
[Date.parse('12/24/2014 02:16:00'), 3747],
[Date.parse('12/24/2014 04:20:00'), 3743],
[Date.parse('12/24/2014 06:16:00'), 3746],
[Date.parse('12/24/2014 08:13:00'), 3758],
[Date.parse('12/24/2014 12:15:00'), 3714],
[Date.parse('12/24/2014 14:22:00'), 3690],
[Date.parse('12/24/2014 16:13:00'), 3667],
[Date.parse('12/24/2014 18:19:00'), 3507],
[Date.parse('12/24/2014 20:14:00'), 3350],
[Date.parse('12/24/2014 22:09:00'), 3242],
[Date.parse('12/25/2014 00:24:00'), 3052],
[Date.parse('12/25/2014 16:23:00'), 3003],
[Date.parse('12/25/2014 18:21:00'), 3049],
[Date.parse('12/25/2014 20:12:00'), 3031],
[Date.parse('12/25/2014 22:08:00'), 3045],
[Date.parse('12/26/2014 00:08:00'), 3027],
[Date.parse('12/26/2014 02:17:00'), 3034],
[Date.parse('12/26/2014 04:20:00'), 3039],
[Date.parse('12/26/2014 06:12:00'), 2992],
[Date.parse('12/26/2014 08:12:00'), 3010],
[Date.parse('12/26/2014 10:23:00'), 3024],
[Date.parse('12/26/2014 12:23:00'), 3035],
[Date.parse('12/26/2014 14:10:00'), 3035],
[Date.parse('12/26/2014 16:16:00'), 3059],
[Date.parse('12/26/2014 22:09:00'), 3093],
[Date.parse('12/26/2014 23:19:00'), 3033],
[Date.parse('12/27/2014 00:23:00'), 3008],
[Date.parse('12/27/2014 02:18:00'), 3010],
[Date.parse('12/27/2014 04:19:00'), 3018],
[Date.parse('12/27/2014 06:09:00'), 3020],
[Date.parse('12/27/2014 08:11:00'), 3016],
[Date.parse('12/28/2014 02:24:00'), 2897],
[Date.parse('12/28/2014 04:17:00'), 2899],
[Date.parse('12/28/2014 06:18:00'), 2792],
[Date.parse('12/28/2014 08:09:00'), 2652],
[Date.parse('12/28/2014 10:13:00'), 2615],
[Date.parse('12/28/2014 12:15:00'), 2533],
[Date.parse('12/28/2014 14:13:00'), 2569],
[Date.parse('12/29/2014 04:11:00'), 2528],
[Date.parse('12/29/2014 12:21:00'), 2564],
[Date.parse('12/29/2014 16:20:00'), 2531],
[Date.parse('12/29/2014 18:19:00'), 2524],
[Date.parse('12/29/2014 20:11:00'), 2551],
[Date.parse('12/29/2014 22:33:00'), 2477],
[Date.parse('12/30/2014 08:13:00'), 2454],
[Date.parse('12/30/2014 10:24:00'), 2407],
[Date.parse('12/30/2014 12:10:00'), 2382],
[Date.parse('12/30/2014 14:15:00'), 2269],
[Date.parse('12/31/2014 06:17:00'), 2206],
[Date.parse('12/31/2014 08:16:00'), 2220],
[Date.parse('12/31/2014 12:22:00'), 2129],
[Date.parse('12/31/2014 14:19:00'), 2097],
[Date.parse('12/31/2014 16:18:00'), 2076],
[Date.parse('12/31/2014 18:24:00'), 2084],
[Date.parse('12/31/2014 22:14:00'), 2129],
[Date.parse('01/01/2015 08:11:00'), 2107],
[Date.parse('01/01/2015 14:20:00'), 1978],
[Date.parse('01/01/2015 16:22:00'), 1929],
[Date.parse('01/01/2015 18:24:00'), 1942],
[Date.parse('01/02/2015 06:19:00'), 1799],
[Date.parse('01/02/2015 08:13:00'), 1802],
[Date.parse('01/02/2015 10:16:00'), 1736],
[Date.parse('01/02/2015 12:22:00'), 1694],
[Date.parse('01/02/2015 14:23:00'), 1635],
[Date.parse('01/02/2015 16:16:00'), 1652],
[Date.parse('01/02/2015 18:20:00'), 1616],
[Date.parse('01/02/2015 20:16:00'), 1611],
[Date.parse('01/02/2015 22:22:00'), 1572],
[Date.parse('01/03/2015 00:25:00'), 1512],
[Date.parse('01/03/2015 02:20:00'), 1489],
[Date.parse('01/03/2015 10:10:00'), 1516],
[Date.parse('01/03/2015 12:21:00'), 1514],
[Date.parse('01/03/2015 14:15:00'), 1469],
[Date.parse('01/03/2015 16:14:00'), 1451],
[Date.parse('01/03/2015 18:18:00'), 1415],
[Date.parse('01/03/2015 20:18:00'), 1818],
[Date.parse('01/04/2015 00:18:00'), 1446],
[Date.parse('01/04/2015 02:22:00'), 1453],
[Date.parse('01/04/2015 10:12:00'), 1443],
[Date.parse('01/04/2015 12:22:00'), 1424],
[Date.parse('01/04/2015 14:21:00'), 1369],
[Date.parse('01/04/2015 16:22:00'), 1445],
[Date.parse('01/04/2015 18:18:00'), 1453],
[Date.parse('01/04/2015 20:17:00'), 1386],
[Date.parse('01/04/2015 22:20:00'), 1065],
[Date.parse('01/05/2015 10:15:00'), 1068],
[Date.parse('01/05/2015 12:24:00'), 1087],
[Date.parse('01/05/2015 16:20:00'), 1138],
[Date.parse('01/05/2015 18:21:00'), 1075],
[Date.parse('01/05/2015 22:16:00'), 1059],
[Date.parse('01/06/2015 10:16:00'), 1008],
[Date.parse('01/06/2015 12:17:00'), 1003],
[Date.parse('01/06/2015 14:19:00'), 917 ],
[Date.parse('01/06/2015 16:18:00'), 872 ],
[Date.parse('01/06/2015 18:16:00'), 869 ],
[Date.parse('01/06/2015 20:31:00'), 822 ],
[Date.parse('01/06/2015 22:20:00'), 769 ],
[Date.parse('01/07/2015 10:19:00'), 768 ],
[Date.parse('01/07/2015 12:15:00'), 824 ],
[Date.parse('01/07/2015 14:21:00'), 833 ],
[Date.parse('01/07/2015 16:19:00'), 789 ],
[Date.parse('01/07/2015 18:10:00'), 761 ],
[Date.parse('01/07/2015 20:15:00'), 703 ],
[Date.parse('01/07/2015 22:22:00'), 620 ],
[Date.parse('01/08/2015 00:20:00'), 589 ],
[Date.parse('01/08/2015 02:17:00'), 596 ],
[Date.parse('01/08/2015 06:21:00'), 604 ],
[Date.parse('01/08/2015 08:08:00'), 596 ],
[Date.parse('01/08/2015 10:17:00'), 585 ],
[Date.parse('01/08/2015 14:14:00'), 568 ],
[Date.parse('01/08/2015 16:18:00'), 587 ],
[Date.parse('01/08/2015 18:24:00'), 598 ],
[Date.parse('01/08/2015 20:10:00'), 566 ],
[Date.parse('01/08/2015 22:50:00'), 504 ],
[Date.parse('01/09/2015 12:19:00'), 456 ],
[Date.parse('01/09/2015 16:19:00'), 457 ],
[Date.parse('01/09/2015 18:13:00'), 457 ],
[Date.parse('01/09/2015 22:15:00'), 319 ],
[Date.parse('01/10/2015 00:16:00'), 275 ],
[Date.parse('01/10/2015 02:17:00'), 282 ],
[Date.parse('01/10/2015 06:12:00'), 288 ],
[Date.parse('01/10/2015 22:16:00'), 247 ],
[Date.parse('01/11/2015 00:12:00'), 172 ],
[Date.parse('01/11/2015 02:23:00'), 187 ],
[Date.parse('01/11/2015 14:20:00'), 175 ],
[Date.parse('01/11/2015 16:17:00'), 217 ],
[Date.parse('01/11/2015 20:16:00'), 159 ],
[Date.parse('01/11/2015 22:24:00'), 131 ],
[Date.parse('01/12/2015 00:12:00'), 84  ],
[Date.parse('01/12/2015 01:32:00'), 96  ],
[Date.parse('01/12/2015 16:21:00'), 37  ],
'''

content = requests.get(
    'https://tr.wikipedia.org/w/index.php?title=Kullan%C4%B1c%C4%B1:Mavrikant_Bot/Bekleyen&action=raw')

lines = content.text.split('\n')

for line in lines:
    value = line.split('* ')[1].split(' - ')[0].replace('.', '')
    date = line.split(' - ')[1].split(' (UTC)')[0].replace('Ocak', '1').replace(u'Şubat', '2').replace(u'Mart',
                                                                                                      '3').replace(
        u'Nisan', '4').replace(u'Mayıs', '5').replace(u'Haziran', '6').replace(u'Temmuz', '7').replace(u'Ağustos',
                                                                                                   '8').replace(u'Eylül',
                                                                                                                '9').replace(
        u'Ekim', '10').replace(u'Kasım', '11').replace(u'Aralık', '12').replace(':',' ').split(' ')
    indexfile+= '[Date.parse(\''+str(date[1])+'/'+str(date[0])+'/'+str(date[2])+' '+str(date[3])+':'+str(date[4])+':00\'), '+str(value)+'],'

indexfile+= '''
]
					}]
				});
			});
		</script>
	</head>
	<body>
		<div id="container" style="height:95vh; margin: 0 auto"></div>
	</body>
</html>
'''

with open("index.html", "w") as text_file:
    text_file.write(indexfile)

print '''
<!DOCTYPE HTML>
<html lang="en-US">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="refresh" content="1;url=https://tools.wmflabs.org/mavrikant/DogrulamaIstatistikleri/">
        <script type="text/javascript">
            window.location.href = "https://tools.wmflabs.org/mavrikant/DogrulamaIstatistikleri/"
        </script>
        <title>Güncellendi! Geri dönülüyor.</title>
    </head>
    <body>
        <!-- Note: don't tell people to `click` the link, just tell them that it is a link. -->
        Grafik güncellendi! Otomatik olarak <a href='https://tools.wmflabs.org/mavrikant/bekleyen/'>grafiğe</a> yönlendiriliyorsunuz.
    </body>
</html>
'''
