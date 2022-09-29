myarticle = "So, yesterday, the American College of Obstetricians and Gynecologists, a non-profit organization representing more than 60,000 physicians, sounded the alarm about a nationwide abortion ban proposed by Republican officials that would put doctors in jail for providing women with essential healthcare. Under Senator Graham’s ban, doctors and providers could be criminalized and sent to jail for performing an abortion to save a woman’s health, providing an abortion to a woman carrying a fetus with little to no chance of survival, offering critical care in the event of a miscarriage, or even treating a rape or incest survivor who has not compiled — complied with medically unnecessary delays or reporting requirements.The ACOG found that bills like Senator Graham’s have no basis in science, that doctors would become less skilled if such a ban was in effect, and it would interfere with patients’ ability to get timely and critical medical care. Now, separately, Jen Klein, the Director of White House Gender Policy, released a memo discussing how, if passed and enacted, this bill would create a nationwide health crisis, threatening the health and lives of women in all 50 states. I said it before and I’ll keep saying it again: This extreme national ban and plan to criminalize doctors is wildly out of step with the American people, and President Biden and Vice President Harris will continue to do everything in their power to protect women’s reproductive rights and expand access to healthcare."

substitutions = {
  "White House":"Pit of Despair",
  "allegedly":"totally",
  "bill":"snap I didn’t screenshot",
  "official":"puppy",
  "congressional":"spaaaaace",
  "Republican":"piano accordionist",
  "Democrat":"chromatic button accordionist",
  "Senator":"magical wizard",
  "Representative":"unmagical wizard",
  "secretary":"eating champion",
  "leaders":"goblins",
  "washington":"Mount Doom",
  "president":"you know, the guy"
  }

for key, value in substitutions.items():
  myarticle = myarticle.replace(key, value)

print(myarticle)