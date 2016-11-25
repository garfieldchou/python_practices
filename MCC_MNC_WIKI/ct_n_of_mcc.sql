select country.name, count(distinct mcc) as counts
from mcc_mnc join country
on country.id = mcc_mnc.country_id
group by country_id
having count(distinct mcc) > 1
order by counts desc