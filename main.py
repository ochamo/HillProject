if __name__ == '__main__':
    import sys
    from app import CifradoHillApp
    application = CifradoHillApp.CifradoHillApp(sys.argv)
    sys.exit(application.exec_())
