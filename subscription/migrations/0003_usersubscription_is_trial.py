from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('subscription', '0002_subscription_currency'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersubscription',
            name='is_trial',
            field=models.BooleanField(default=False, db_index=True),
        ),
    ]
