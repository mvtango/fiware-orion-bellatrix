# From: http://builtoncement.com/2.4/dev/quickstart.html

from cement.core import backend, foundation, controller, handler

# define an application base controller
class MyAppBaseController(controller.CementBaseController):
    class Meta:
        label = 'base'
        description = "FIWARE Orion CLI Interface"

        config_defaults = dict(
            foo='bar',
            some_other_option='my default value',
            )

        arguments = [
            (['-f', '--foo'], dict(action='store', help='the notorious foo option')),
            (['-C'], dict(action='store_true', help='the big C option'))
            ]

    @controller.expose(hide=True, aliases=['run'])
    def default(self):
        self.app.log.info('Inside base.default function.')
        if self.app.pargs.foo:
            self.app.log.info("Recieved option 'foo' with value '%s'." % \
                          self.pargs.foo)

    @controller.expose(help="this command does relatively nothing useful.")
    def command1(self):
        self.app.log.info("Inside base.command1 function.")

    @controller.expose(aliases=['cmd2'], help="more of nothing.")
    def command2(self):
        self.app.log.info("Inside base.command2 function.")

class MyApp(foundation.CementApp):
    class Meta:
        label = 'Bellatrix'
        base_controller = MyAppBaseController

# create the app
app = MyApp()


try:
    # setup the application
    app.setup()

    # run the application
    app.run()
finally:
    # close the app
    app.close()
