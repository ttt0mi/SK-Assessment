world_population = 8217130000
annual_growth_rate= 0.0085

print()
print("\t\t World Population \t World Population Increase")

for years in range(1, 101):

	world_population = (world_population * annual_growth_rate) + world_population
	world_population_increase = world_population * annual_growth_rate

	print(f"after year {years} \t {world_population:,.0f}     \t {world_population_increase:,.0f}")




























"""
	if(world_population / 8217130000 >= 2):
		world_population_doubled = years

print()
print(world_population_doubled)

"""