import re

import requests
URL_BASE = 'http://www.hel.fi/palvelukarttaws/rest/v4/'


def pk_get(resource_name, res_id=None, v3=False):
    url = "%s%s/" % (URL_BASE, resource_name)
    if res_id is not None:
        url = "%s%s/" % (url, res_id)
    if v3:
        url = url.replace('v4', 'v3')
    resp = requests.get(url)
    assert resp.status_code == 200, 'fuu status code {}'.format(resp.status_code)
    return resp.json()


def save_translated_field(obj, obj_field_name, info, info_field_name, max_length=None):
    args = {}
    has_changed = False
    for lang in ('fi', 'sv', 'en'):
        key = '%s_%s' % (info_field_name, lang)
        if key in info:
            val = clean_text(info[key])
        else:
            val = None
        if max_length and val and len(val) > max_length:
            # if self.verbosity:
            #     self.logger.warning("%s: field '%s' too long" % (obj, obj_field_name))
            val = None
        obj_key = '%s_%s' % (obj_field_name, lang)
        obj_val = getattr(obj, obj_key, None)
        if obj_val == val:
            continue

        setattr(obj, obj_key, val)
        if lang == 'fi':
            setattr(obj, obj_field_name, val)
        has_changed = True
    return has_changed


def clean_text(text):
    # remove consecutive whitespaces
    text = re.sub(r'\s\s+', ' ', text, re.U)
    # remove nil bytes
    text = text.replace('\u0000', ' ')
    text = text.strip()
    return text
