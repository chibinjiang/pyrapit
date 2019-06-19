# -*- coding: utf-8 -*-
from rapit.behaviors import Behavior


class CreateAudienceLanguage(Behavior):
    name = 'create_audience_language'


class CreateAudienceLocation(Behavior):
    name = 'create_audience_location'


class CreateAudienceAge(Behavior):
    name = 'create_audience_age'


class GenerateAudience(Behavior):
    name = 'generate_audience'


name_behavior_map = {
    CreateAudienceLanguage.name: CreateAudienceLanguage
}