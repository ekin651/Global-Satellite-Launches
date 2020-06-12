#!/bin/sh

red=$'\e[1;31m'
grn=$'\e[1;32m'
yel=$'\e[1;33m'
mag=$'\e[1;35m'
cyn=$'\e[1;36m'
nc=$'\e[0m'
lgrn=$'\e[92m'
blink=$'\e[5m'
noblink= $'\e[25m'

bold=$'\e[1m' 
nobold=$'\e[21m'


echo Brought to you by: ${cyn}Henry Le${nc}
echo -e Version: ${mag}0${nc}, Date: ${mag}Jun, 2020${nc}
echo =============================
echo
while true
do 
	echo -e "${red}${blink}${bold}WARNING${nobold}${noblink}${nc} :: ${yel}Data may be lost${nc} if push incorrectly!"
	read -r -p "Are you ${cyn}sure${nc} you want to push (y/n)?${nc}" userinput
	case $userinput in 
	
		[yY][eE][sS]|[yY])
			echo Begin ${red}Git Pushing${nc}. Please wait...
			echo ---------------
			echo ${yel}Adding files...${nc} & git add .
			echo ---------------
			echo "${yel}Preparing to push...${nc}" 
			echo ---------------
			echo Please ${red}input message${nc} "(${red}NO ${cyn}double quote${nc} needed)"
			read message
			echo Adding message... & git commit -m "$message"
			echo ---------------
			echo "Message: ${cyn}$message${nc} - sucessfully added"
			echo ---------------
			echo ${yel}UPLOADING FILES${nc} ... Please wait ...
			echo ---------------
			git push
			echo
			echo ================================
			echo
			echo
			break
		;;
		
		[nN][oO]|[nN])
			echo
			echo ================================
			echo
			echo "${yel}Nothing was pushed${nc}"
			echo
			echo ================================
			echo
			break
		;;
		
		*)
			echo "--------------------------"
			echo "${red}In Valid Input ... ${nc}"
			echo "${cyn}Please try again ... ${nc}"
			echo "--------------------------"
			
		;;	
	esac
done

echo "${lgrn}  FINISHED${nc}. Please hit ${yel}Enter${nc} to exit."

read


