import tornado.web
import tornado.ioloop
from apiApplicationModel import userData
from cleanArray import Label_Correction

colName=['age', 'resting_blood_pressure', 'cholesterol', 'max_heart_rate_achieved', 'st_depression', 'num_major_vessels', 'st_slope_downsloping', 'st_slope_flat', 'st_slope_upsloping', 'sex_male', 'chest_pain_type_atypical angina', 'chest_pain_type_non-anginal pain', 'chest_pain_type_typical angina', 'fasting_blood_sugar_lower than 120mg/ml', 'rest_ecg_left ventricular hypertrophy', 'rest_ecg_normal', 'exercise_induced_angina_yes', 'thalassemia_fixed defect', 'thalassemia_normal',
       'thalassemia_reversable defect']

class basicRequestHandler(tornado.web.RequestHandler):

  def get(self):
    self.render('report.html')

class staticRequestHandler(tornado.web.RequestHandler):

  def post(self):
      data_input_array = []
      for name in colName:
          x = self.get_body_argument(name, default=0)
          data_input_array.append(int(x))
      label = Label_Correction(data_input_array)
      finalResult = userData(label)
      if(finalResult==1):
          self.render("fail_page.html")
      else:
          self.render("success_page.html")

if __name__=='__main__':
  app = tornado.web.Application([(r"/",basicRequestHandler),
                                 (r"/result",staticRequestHandler)])
  print("API IS RUNNING.......")
  app.listen(8887)
  tornado.ioloop.IOLoop.current().start()