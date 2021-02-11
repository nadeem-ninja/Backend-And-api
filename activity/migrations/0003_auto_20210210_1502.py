# Generated by Django 3.1.6 on 2021-02-10 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0002_auto_20210210_0927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='tz',
            field=models.CharField(choices=[('Samoa and Christmas Island/Kiribati', 'UTC +14'), ('Chatham Islands/New Zealand', 'UTC +13:45'), ('New Zealand with exceptions and 4 more', 'UTC +13'), ('Fiji, small region of Russia and 7 more', 'UTC +12'), ('much of Australia and 7 more', 'UTC +11'), ('small region of Australia', 'UTC +10:30'), ('Queensland/Australia and 6 more', 'UTC +10'), ('Northern Territory/Australia', 'UTC +9:30'), ('Japan, South Korea and 5 more', 'UTC +9'), ('Western Australia/Australia', 'UTC +8:45'), ('China, Philippines and 10 more', 'UTC +8'), ('much of Indonesia, Thailand and 7 more', 'UTC +7'), ('Myanmar and Cocos Islands', 'UTC +6:30'), ('Bangladesh and 6 more', 'UTC +6'), ('Nepal', 'UTC +5:45'), ('India and Sri Lanka', 'UTC +5:30'), ('Pakistan and 8 more', 'UTC +5'), ('Afghanistan', 'UTC +4:30'), ('Azerbaijan and 8 more', 'UTC +4'), ('Iran', 'UTC +3:30'), ('Moscow/Russia, Turkey and 20 more', 'UTC +3'), ('Greece and 32 more', 'UTC +2'), ('Germany and 45 more', 'UTC +1'), ('United Kingdom and 24 more', 'UTC +0'), ('Cabo Verde and 2 more', 'UTC -1'), ('Pernambuco/Brazil and South Georgia/Sandwich Is.', 'UTC -2'), ('most of Brazil, Argentina and 9 more', 'UTC -3'), ('Newfoundland and Labrador/Canada', 'UTC -3:30'), ('some regions of Canada and 28 more', 'UTC -4'), ('regions of USA and 14 more', 'UTC -5'), ('some regions of USA and 9 more', 'UTC -6'), ('some regions of USA and 2 more', 'UTC -7'), ('regions of USA and 4 more', 'UTC -8'), ('Alaska/USA and regions of French Polynesia', 'UTC -9'), ('Marquesas Islands/French Polynesia', 'UTC -9:30'), ('small region of USA and 2 more', 'UTC -10'), ('American Samoa and 2 more', 'UTC -11'), ('much of US Minor Outlying Islands', 'UTC -12')], max_length=50),
        ),
    ]
