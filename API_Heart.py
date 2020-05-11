import tornado.web
import tornado.ioloop
from apiApplicationModel import userData
from cleanArray import Label_Correction
import json
import asyncio
import aiohttp

colName=['age', 'resting_blood_pressure', 'cholesterol', 'max_heart_rate_achieved', 'st_depression', 'num_major_vessels', 'st_slope_downsloping', 'st_slope_flat', 'st_slope_upsloping', 'sex_male', 'chest_pain_type_atypical angina', 'chest_pain_type_non-anginal pain', 'chest_pain_type_typical angina', 'fasting_blood_sugar_lower than 120mg/ml', 'rest_ecg_left ventricular hypertrophy', 'rest_ecg_normal', 'exercise_induced_angina_yes', 'thalassemia_fixed defect', 'thalassemia_normal',
       'thalassemia_reversable defect']

class processRequestHandler(tornado.web.RequestHandler):
    def post(self):
        data_input_array = []
        for name in colName:
            x = self.get_body_argument(name, default=0)
            data_input_array.append(int(x))
        label = Label_Correction(data_input_array)
        finalResult = int(userData(label))
        output = json.dumps({"Giveput":finalResult})
        self.write(output)

class basicRequestHandler(tornado.web.RequestHandler):

  def get(self):
    self.render('report.html')


cr=None

def get_count():
    global cr
    if cr:
        return cr+1
    cr = 1
    return cr

class staticRequestHandler(tornado.web.RequestHandler):
  counter =1
  async def post(self):
      x= self.request.body
      url = "http://localhost:8887/output"
      async with aiohttp.ClientSession() as session:
          response = await session.post(url=url,data=x)
      final = await response.read()
      final = json.loads((final).decode('utf-8'))
      if final['Giveput'] == 0:
          self.render('Success_page.html')
          print(get_count(),"Results shown")

      else:
          self.render('fail_page.html')
          print(get_count(),"Results shown")



if __name__=='__main__':
  app = tornado.web.Application([(r"/",basicRequestHandler),
                                 (r"/result",staticRequestHandler),
                                 (r"/output",processRequestHandler)])
  print("API IS RUNNING.......")
  server = tornado.httpserver.HTTPServer(app)
  server.bind(8887, '127.0.0.1')
  server.start()
  asyncio.get_event_loop().run_forever()
