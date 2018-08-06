"""
We use this validator to filter ip that can access mobile bili website.
"""
from haipproxy.config.settings import (
    TEMP_BILI_QUEUE, VALIDATED_BILI_QUEUE,
    TTL_BILI_QUEUE, SPEED_BILI_QUEUE)
from ..redis_spiders import ValidatorRedisSpider
from .base import BaseValidator


class BiliValidator(BaseValidator, ValidatorRedisSpider):
    """This validator checks the liveness of bili proxy resources"""
    name = 'bili'
    urls = [
        'http://api.live.bilibili.com/lottery/v1/Storm/join',
        'https://api.live.bilibili.com/lottery/v1/Storm/join',
    ]
    task_queue = TEMP_BILI_QUEUE
    score_queue = VALIDATED_BILI_QUEUE
    ttl_queue = TTL_BILI_QUEUE
    speed_queue = SPEED_BILI_QUEUE
    success_key = '节奏风暴不存在'
