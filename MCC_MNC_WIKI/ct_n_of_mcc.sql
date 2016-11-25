select country_id, count(distinct mcc)
from mcc_mnc
group by country_id
having count(distinct mcc) > 1