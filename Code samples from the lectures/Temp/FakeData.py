from __future__ import unicode_literals

from faker import Factory
import random
fake = Factory.create('nl_NL')
for a in "abcdefghijklmnopqrstuvwxyz1234567890":
    print "student{} = Student(\"{}\", {})".format(a, fake.name(),random.randint(1, 10))
