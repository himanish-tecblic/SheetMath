from app.models import PBPM
always_space = 0 # in percentage
whs = 1000 # whs 
other = 100
insurance = 1 # in a percentage
no_of_bag_utilization = 100 #in  percentage
overhead_per_ten_mt = 10
fumigation = 13 
profit = 20 #in a percentage
profit_in_mt = 25 #ina percenatage
def calc_pbm(ft,id):
    pbpm = PBPM.objects.get(id=id)
    pbpm.ft = ft
    pbpm.rent = pbpm.rate * ft
    pbpm.rent_per_mt = pbpm.rent / pbpm.utilize_mt
    pbpm.allway_space = ft * always_space
    pbpm.net_space = ft - pbpm.allway_space
    pbpm.utilisation = pbpm.net_space * pbpm.space_per_bag * pbpm.stack_ht
    pbpm.wh_capacity = (pbpm.utilisation * pbpm.bag_size) / 1000
    pbpm.value_per_bag = (pbpm.commodity_rate / 1000) * pbpm.bag_size
    pbpm.whs = whs
    pbpm.whs_per_mt = pbpm.whs / pbpm.utilize_mt
    pbpm.sg = pbpm.whs_per_mt
    pbpm.sg_per_mt = pbpm.sg / pbpm.utilize_mt
    pbpm.other = other
    pbpm.no_of_bag_utilization = pbpm.wh_capacity * no_of_bag_utilization
    pbpm.utilize_mt = (pbpm.no_of_bag_utilization * pbpm.bag_size) / 1000
    pbpm.total_value = pbpm.no_of_bag_utilization * pbpm.value_per_bag
    pbpm.insurance = pbpm.total_value * insurance
    pbpm.insurance_per_month = pbpm.insurance / 12
    pbpm.insurance_per_mt = pbpm.insurance_per_month / pbpm.utilize_mt
    pbpm.fumigation = (pbpm.no_of_bag_utilization * pbpm.bag_size )/ 1000 * fumigation
    pbpm.fumigation_per_mt = pbpm.fumigation / pbpm.insurance_per_mt
    pbpm.overhead_per_ten_mt = pbpm.utilize_mt * overhead_per_ten_mt
    pbpm.overhead_per_mt = pbpm.overhead_per_ten_mt / pbpm.utilize_mt
    pbpm.total_cost = pbpm.whs + pbpm.sg + pbpm.insurance_per_month + pbpm.fumigation_per_mt + pbpm.overhead_per_ten_mt + pbpm.rent
    pbpm.cost_per_bag = pbpm.total_cost / pbpm.no_of_bag_utilization
    pbpm.profit = pbpm.cost_per_bag  * profit
    pbpm.base_rate_pbpm = pbpm.cost_per_bag + pbpm.profit
    pbpm.base_rate_per_mt = (pbpm.cost_per_bag * 1000) / pbpm.bag_size
    pbpm.profit_in_mt = pbpm.base_rate_per_mt * profit_in_mt
    pbpm.base_rate_pmt = pbpm.profit_in_mt + pbpm.base_rate_per_mt
    pbpm.save()
    return pbpm