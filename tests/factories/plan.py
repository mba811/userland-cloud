from factory import Factory, Trait
from pytest_factoryboy import register

from app.models import Plan


@register
class PlanFactory(Factory):
    class Meta:
        model = Plan

    box_count = 5
    bandwidth = 100000
    forwards = 9999
    reserved_config = 5
    cost = 999
    name = "paid"
    # NOTE If you delete the plan on the test account, you are going to need to
    # update this plan id
    stripe_id = "plan_FZrbLVsKMsw3IL"

    class Params:
        paid = True

        free = Trait(
            box_count=1,
            bandwidth=100,
            forwards=2,
            reserved_config=0,
            cost=0,
            name="free",
            stripe_id=None,
        )

        waiting = Trait(
            box_count=0,
            bandwidth=0,
            forwards=0,
            reserved_config=0,
            cost=0,
            name="waiting",
            stripe_id=None,
        )

        beta = Trait(
            box_count=2,
            bandwidth=1000,
            forwards=10,
            reserved_config=1,
            cost=0,
            name="beta",
            stripe_id=None,
        )

        admin = Trait(
            box_count=20,
            bandwidth=10000,
            forwards=100,
            reserved_config=1,
            cost=0,
            name="admin",
            stripe_id=None,
        )
