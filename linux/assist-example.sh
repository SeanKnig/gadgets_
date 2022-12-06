function rerun_tether() {
    cd automation
    #scp /path/to/file username@a:/path/to/destination
    #scp ./tether_v0.py autplayground@:/path/to/destination
    #ssh user_name@host
    sudo rm -rf control_panel/ django_core/ manage.py tenv/ tmp/
    python3 -m venv tenv
    source tenv/bin/activate
    pip install -r requirements.txt
    python3 tether_v0.py
    python3 switch_tether.py
    sudo rm -rf control_panel/tools/ control_panel/backup/ control_panel/frontend/
    python3 tether_v0_testout.py
}
function reset_tether() {
    cd automation
    sudo rm -rf control_panel/ django_core/ manage.py tenv/ tmp/ db.sqlite3
}
function execute_tether() {
  cd automation
  python3 -m venv tenv
  source tenv/bin/activate
  pip install -r requirements.txt
  python3 build_app_arch.py
  sudo chown -R <>:<> ./*
  sleep 15
  python3 extract_map.py
}
function build_app_arch() {
  cd automation
  python3 -m venv tenv
  source tenv/bin/activate
  pip install -r requirements.txt
  python3 build_app_arch.py
  python3 extract_map.py
}
function extract_map() {
  cd automation
  source tenv/bin/activate
  python3 extract_map.py
}
case $* in
--reset_tether|-r)
  reset_tether
;;
--rerun_tether|-rr)
  rerun_tether
;;
--build_app_arch|-baa)
  build_app_arch
;;
--extract_app_map|-em)
  extract_map
;;
--execute_tether|-et)
  execute_tether
;;
*)
help
;;
esac
exit 0
