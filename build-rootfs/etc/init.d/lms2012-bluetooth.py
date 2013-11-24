#!/usr/bin/python

import gobject


import dbus
import dbus.service
import dbus.mainloop.glib







class Rejected(dbus.DBusException):
    _dbus_error_name = "org.bluez.Error.Rejected"

class Agent(dbus.service.Object):
    exit_on_release = True

    def set_exit_on_release(self, exit_on_release):
        self.exit_on_release = exit_on_release

    @dbus.service.method("org.bluez.Agent",
                    in_signature="", out_signature="")
    def Release(self):
        print "Release"
        if self.exit_on_release:
            mainloop.quit()

    @dbus.service.method("org.bluez.Agent",
                    in_signature="os", out_signature="")
    def Authorize(self, device, uuid):
        print "Authorize (%s, %s)" % (device, uuid)
        return

    @dbus.service.method("org.bluez.Agent",
                    in_signature="o", out_signature="s")
    def RequestPinCode(self, device):
        print "RequestPinCode (%s)" % (device)
        return "1234"

    @dbus.service.method("org.bluez.Agent",
                    in_signature="o", out_signature="u")
    def RequestPasskey(self, device):
        print "RequestPasskey (%s)" % (device)
        passkey = 1234
        return dbus.UInt32(passkey)

    @dbus.service.method("org.bluez.Agent",
                    in_signature="ou", out_signature="")
    def DisplayPasskey(self, device, passkey):
        print "DisplayPasskey (%s, %d)" % (device, passkey)

    @dbus.service.method("org.bluez.Agent",
                    in_signature="ou", out_signature="")
    def RequestConfirmation(self, device, passkey):
        print "RequestConfirmation (%s, %d)" % (device, passkey)
        return
        

    @dbus.service.method("org.bluez.Agent",
                    in_signature="s", out_signature="")
    def ConfirmModeChange(self, mode):
        print "ConfirmModeChange (%s)" % (mode)        
        return
        

    @dbus.service.method("org.bluez.Agent",
                    in_signature="", out_signature="")
    def Cancel(self):
        print "Cancel"

def create_device_reply(device):
    print "New device (%s)" % (device)
    mainloop.quit()

def create_device_error(error):
    print "Creating device failed: %s" % (error)
    mainloop.quit()

if __name__ == '__main__':
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)

    bus = dbus.SystemBus()
    manager = dbus.Interface(bus.get_object("org.bluez", "/"),
                                                     "org.bluez.Manager")
    adapter_path = manager.DefaultAdapter()

    adapter= dbus.Interface(bus.get_object("org.bluez", adapter_path),
                                                      "org.bluez.Adapter")
    adapter.SetProperty("Discoverable",True)

    network_server = dbus.Interface(bus.get_object("org.bluez", adapter_path),
                                                     "org.bluez.NetworkServer")
    network = network_server.Register("nap" ,"br0")

    capability = "NoInputNoOutput"
    

  
    path = "/ev3/agent"
    agent = Agent(bus, path)

    mainloop = gobject.MainLoop()

    adapter.RegisterAgent(path, capability)
    print "Agent registered"

    mainloop.run()

    #adapter.UnregisterAgent(path)
    #print "Agent unregistered"
