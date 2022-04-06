"""



"""
import requests
from lxml import etree


class Entity(dict):
    """
    It works like a normal dict but values can be accessed as attribute.
    """

    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError:
            raise AttributeError("No such key '%s'" % name)

    __setattr__ = dict.__setitem__

    def __delattr__(self, name):
        try:
            del self[name]
        except KeyError:
            raise AttributeError("No such key '%s'" % name)


def parse_team_members(xml_content):
    t = etree.fromstring(xml_content)

    results = []
    for member in t.getchildren():
        is_admin = bool("admin" in member.tag)
        user_name = member.findtext("s:username", None, t.nsmap)
        nickname = member.findtext("s:nickname", None, t.nsmap)
        storage_quota = member.findtext("s:storage_quota", None, t.nsmap)
        storage_quota = int(storage_quota) if storage_quota else None
        ldap_user = member.findtext("s:ldap_user", None, t.nsmap)
        ldap_user = ldap_user == "true" if ldap_user else None
        disabled = member.findtext("s:disabled", None, t.nsmap)
        disabled = disabled == "true" if disabled else None
        entity = Entity(admin=is_admin,
                        user_name=user_name,
                        nickname=nickname,
                        storage_quota=storage_quota,
                        ldap_user=ldap_user,
                        disabled=disabled)
        results.append(entity)

    def check_disabled(results):
        return not results['disabled']

    return list(filter(check_disabled, results))


# for member in parse_team_members(content):
#     print(member.username)

if __name__ == '__main__':
    content = requests.get("https://dav-demo.jianguoyun.com/nsdav/getTeamMembers", auth=("yangyuying+8@nutstore.net", "")).content
    print(parse_team_members(content))