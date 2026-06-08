#!/bin/bash

# This test file will be automatically run when you submit a pull request
# You should not modify this file
# You can run this file using ./test-sdc.sh task-directory-name to check your output

echo "<!--CYFTT tag: sdc-test-results-->" > testoutput.txt
echo "Results of test:" >> testoutput.txt

if [[ "$1" == "individual-shell-tools" ]]; then
	cd individual-shell-tools
	pass=0
	total=0
	for directory in */; do
		cd $directory
		if [ "$directory" == "helper-files/" ]; then
			cd ..
			continue
		fi
		for exercise in *.sh; do
			total=$(($total+1))
			./$exercise > ../../test.tmp
			cmp ../../test.tmp ../../expect/individual-shell-tools/$directory$exercise
			if [ $? -eq 0 ]; then
				pass=$(($pass+1))
			else
				if [[ "$exercise" == *"stretch"* && $(stat -c%s ../../test.tmp) == "0" ]]; then
					# Stretch task not attempted, ignoring"
					total=$(($total-1))
				else
					echo "Failed $directory$exercise, please check" >> ../../testoutput.txt
				fi
			fi
		done
		cd ..
	done
	cd ..
	rm test.tmp
	echo "You passed $pass/$total tasks." >> testoutput.txt
	if [ -v GITHUB_OUTPUT ]; then
		echo "attempted=y" >> "$GITHUB_OUTPUT"
	fi
	if [ $pass -ge $total ]; then
		echo "This task is complete!" >> testoutput.txt
		if [ -v GITHUB_OUTPUT ]; then
			echo "complete=y" >> "$GITHUB_OUTPUT"
		fi
	fi
	cat testoutput.txt
elif [[ "$1" == "shell-pipelines" ]]; then
	cd shell-pipelines
	pass=0
	total=0
	for directory in */; do
		cd $directory
		for exercise in *.sh; do
			total=$(($total+1))
			./$exercise > ../../test.tmp
			cmp ../../test.tmp ../../expect/shell-pipelines/$directory$exercise
			if [ $? -eq 0 ]; then
				pass=$(($pass+1))
			else
				echo "Failed $directory$exercise, please check" >> ../../testoutput.txt
			fi
		done
		cd ..
	done
	cd ..
	rm test.tmp
	echo "You passed $pass/$total tasks." >> testoutput.txt
	if [ -v GITHUB_OUTPUT ]; then
		echo "attempted=y" >> "$GITHUB_OUTPUT"
	fi
	if [ $pass -eq $total ]; then
		echo "This task is complete!" >> testoutput.txt
		if [ -v GITHUB_OUTPUT ]; then
			echo "complete=y" >> "$GITHUB_OUTPUT"
		fi
	fi
	cat testoutput.txt
elif [[ "$1" == "jq" ]]; then
	cd jq
	pass=0
	total=0
	for exercise in *.sh; do
		total=$(($total+1))
		./$exercise > ../test.tmp
		cmp ../test.tmp ../expect/jq/$exercise
		if [ $? -eq 0 ]; then
			pass=$(($pass+1))
		else
			echo "Failed $exercise, please check" >> ../testoutput.txt
		fi
	done
	cd ..
	rm test.tmp
	echo "You passed $pass/$total tasks." >> testoutput.txt
	if [ -v GITHUB_OUTPUT ]; then
		echo "attempted=y" >> "$GITHUB_OUTPUT"
	fi
	if [ $pass -eq $total ]; then
		echo "This task is complete!" >> testoutput.txt
		if [ -v GITHUB_OUTPUT ]; then
			echo "complete=y" >> "$GITHUB_OUTPUT"
		fi
	fi
	cat testoutput.txt
elif [[ "$1" == "number-systems" ]]; then
	pass=0
	for question in $(seq 1 15); do
		answer=$(jq -r ".answers[$question]" expect/number-systems/Part-1.json)
		nextq=$(($question+1))
		Q_START=$(grep -n "Q$question:" number-systems/Part-1.md | cut -d: -f1)
		ANS_START=$(($Q_START + 1))
		NEXT_Q_START=$(grep -n "Q$nextq:" number-systems/Part-1.md | cut -d: -f1)
		ANS_END=$(($NEXT_Q_START - 1))
		sed -n "$ANS_START,${ANS_END}p;${NEXT_Q_START}q" number-systems/Part-1.md | cut -d: -f2- > answerfile
		grep --quiet -iE $answer answerfile
		if [ $? -eq 0 ]; then
			pass=$(($pass+1))
		else
			echo "Q$question incorrect, please check" >> testoutput.txt
		fi
		rm answerfile
	done
	echo "You passed $pass/15 tasks in part 1." >> testoutput.txt
	if [ -v GITHUB_OUTPUT ]; then
		echo "attempted=y" >> "$GITHUB_OUTPUT"
	fi
	echo "Please let a volunteer check the answers for part 2." >> testoutput.txt
	cat testoutput.txt
elif [[ "$1" == "implement-cowsay" ]]; then
  if [ -v GITHUB_OUTPUT ]; then
    echo "attempted=y" >> "$GITHUB_OUTPUT"
  fi
  if [[ -e .cowsay-venv ]]; then
    echo ".cowsay-venv already exists - couldn't test cowsay" >> testoutput.txt
  else
    if [ ! -e implement-cowsay/requirements.txt ]; then
      echo "Expected implement-cowsay/requirements.txt to exist but it didn't" >> testoutput.txt
    else
      python3 -m venv .cowsay-venv
      . .cowsay-venv/bin/activate
      pip3 install -r implement-cowsay/requirements.txt

      all_ok=true

      python3 implement-cowsay/cow.py Grass, delicious > test.tmp
      cmp test.tmp expect/implement-cowsay/cow-grass.txt
      if [ $? -ne 0 ]; then
        echo "Unexpected cowsay output for 'Grass, delicious'." >> testoutput.txt
        all_ok=false
      fi

      python3 implement-cowsay/cow.py --animal turtle "Fish are cool!" > test.tmp
      cmp test.tmp expect/implement-cowsay/turtle-fish.txt
      if [ $? -ne 0 ]; then
        echo "Unexpected cowsay output for --animal turtle Fish are cool!" >> testoutput.txt
        all_ok=false
      fi

      python3 implement-cowsay/cow.py --help | grep dragon
      if [ $? -ne 0 ]; then
        echo "Expected python3 cow.py --help to include dragon as it's one of the animal options" >> testoutput.txt
        all_ok=false
      fi

      grep dragon implement-cowsay/cow.py > /dev/null
      if [ $? -eq 0 ]; then
        echo "Didn't expect cow.py to include the word dragon - you should pull in the animal options from the library not write them yourself" >> testoutput.txt
        all_ok=false
      fi

      if [[ "${all_ok}" == "true" && -v GITHUB_OUTPUT ]]; then
        echo "complete=y" >> "$GITHUB_OUTPUT"
        echo "Your implementation passed all checks." >> testoutput.txt
      fi
    fi
  fi
else
	echo "Please run this with a valid test directory name as argument"
fi
