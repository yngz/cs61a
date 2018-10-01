test = {
  'name': 'Car',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from car import *
          >>> deneros_car = Car('Tesla', 'Model S')
          >>> deneros_car.color
          'No color yet. You need to paint me.'
          >>> deneros_car.paint('black')
          'Tesla Model S is now black'
          >>> deneros_car.color
          'black'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> from car import *
          >>> deneros_car = Car('Tesla', 'Model S')
          >>> deneros_car.model
          'Model S'
          >>> deneros_car.gas = 10
          >>> deneros_car.drive()
          'Tesla Model S goes vroom!'
          >>> deneros_car.drive()
          'Tesla Model S cannot drive!'
          >>> deneros_car.fill_gas()
          'Tesla Model S gas level: 20'
          >>> deneros_car.gas
          20
          >>> Car.gas
          30
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> from car import *
          >>> deneros_car = Car('Tesla', 'Model S')
          >>> Car.headlights
          2
          >>> deneros_car.headlights
          2
          >>> Car.headlights = 3
          >>> deneros_car.headlights
          3
          >>> deneros_car.headlights = 2
          >>> Car.headlights
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> from car import *
          >>> deneros_car = Car('Tesla', 'Model S')
          >>> deneros_car.wheels = 2
          >>> deneros_car.wheels
          2
          >>> Car.num_wheels
          4
          >>> deneros_car.drive() # Type Error if an error occurs and Nothing if nothing is displayed
          'Tesla Model S cannot drive!'
          >>> Car.drive() # Type Error if an error occurs and Nothing if nothing is displayed
          Error
          >>> Car.drive(deneros_car) # Type Error if an error occurs and Nothing if nothing is displayed
          'Tesla Model S cannot drive!'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> from car import *
          >>> deneros_car = MonsterTruck('Monster', 'Batmobile')
          >>> deneros_car.drive() # Type Error if an error occurs and Nothing if nothing is displayed
          Vroom! This Monster Truck is huge!
          'Monster Batmobile goes vroom!'
          >>> Car.drive(deneros_car) # Type Error if an error occurs and Nothing if nothing is displayed
          'Monster Batmobile goes vroom!'
          >>> MonsterTruck.drive(deneros_car) # Type Error if an error occurs and Nothing if nothing is displayed
          Vroom! This Monster Truck is huge!
          'Monster Batmobile goes vroom!'
          >>> Car.rev(deneros_car) # Type Error if an error occurs and Nothing if nothing is displayed
          Error
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
