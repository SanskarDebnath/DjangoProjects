# Generated by Django 4.2.7 on 2024-02-10 04:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_productcategory_delete_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='product.productcategory'),
        ),
    ]