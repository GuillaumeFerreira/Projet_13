# Generated by Django 3.2.5 on 2022-09-18 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("lettings", "0002_alter_letting_address"),
    ]

    operations = [
        migrations.RunSQL(
            """
                INSERT INTO lettings_address (
                    id,
                    number,
                    street,
                    city,
                    state,
                    zip_code ,
                    country_iso_code
                )
                SELECT
                    id,
                    number,
                    street,
                    city,
                    state,
                    zip_code ,
                    country_iso_code
                FROM
                    oc_lettings_site_letting;
            """,
            reverse_sql="""
                INSERT INTO oc_lettings_site_letting (
                    id,
                    number,
                    street,
                    city,
                    state,
                    zip_code ,
                    country_iso_code
                )
                SELECT
                    id,
                    number,
                    street,
                    city,
                    state,
                    zip_code ,
                    country_iso_code
                FROM
                    lettings_address;
            """,
        )
    ]
