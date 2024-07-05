from twisted.cred.checkers import AllowAnonymousAccess, InMemoryUsernamePasswordDatabaseDontUse
from twisted.cred.portal import Portal
from twisted.internet import reactor
from twisted.protocols.ftp import FTPFactory, FTPRealm

class MyFTPFactory(FTPFactory):
    def startFactory(self):
        print("Servidor FTP activo en el hostname: 127.0.0.1")
        print("Servidor FTP activo en el puerto: 8080")


checker = InMemoryUsernamePasswordDatabaseDontUse()
checker.addUser("ricardo", '2708')
checker.addUser("someuser", '2708')

portal = Portal(FTPRealm('./public', './myusers'), [AllowAnonymousAccess(), checker])

factory = MyFTPFactory(portal)

reactor.listenTCP(8080, factory)
reactor.run()