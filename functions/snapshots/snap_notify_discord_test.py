# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot

snapshots = Snapshot()

snapshots[
    "test_event_get_slack_message_payload_snapshots event_cloudwatch_alarm.json"
] = [
    {
        "username": "AWS",
        "avatar_url": "https://i.imgur.com/eeYUFCO_d.webp",
        "content": "New AWS Notification",
        "embeds": [
            {
                "author": {
                    "name": "Cloudwatch Alarm",
                    "url": "https://console.aws.amazon.com/cloudwatch/home?region=us-east-1",
                    "icon_url": "https://i.imgur.com/llpFFJc_d.webp"
                },
                "title": "DBMigrationRequired",
                "url": "https://console.aws.amazon.com/cloudwatch/home?region=us-east-1",
                "description": "App is reporting 'A JPA error occurred(Unable to build EntityManagerFactory)'",
                "color": "16761600",
                "fields": [
                    {
                        "name": "Alarm Description",
                        "value": "`App is reporting 'A JPA error occurred(Unable to build EntityManagerFactory)'`"
                    },
                    {
                        "name": "Alarm reason",
                        "value": "`Threshold Crossed: 1 datapoint [1.0 (12/02/19 15:44:00)] was not less than the threshold (1.0).`"
                    },
                    {
                        "name": "Old State",
                        "value": "`ALARM`",
                        "inline": "true"
                    },
                    {
                        "name": "Current State",
                        "value": "`OK`",
                        "inline": "true"
                    },
                    {
                        "name": "Link to Alarm",
                        "value": "https://console.aws.amazon.com/cloudwatch/home?region=us-east-1#alarm:alarmFilter=ANY;name=DBMigrationRequired"
                    }
                ],
                "thumbnail": {
                    "url": "https://i.imgur.com/llpFFJc_d.webp"
                },
                "footer": {
                    "text": "AWS CloudWatch notification - DBMigrationRequired"
                }
            }
        ]
    }
]
