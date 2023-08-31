for protoname in reaction dataset
do
  wget https://raw.githubusercontent.com/open-reaction-database/ord-schema/main/proto/$protoname.proto
  if [[ $protoname == dataset ]]
  then
    sed -i 's/ord-schema\/proto\/reaction.proto/reaction.proto/' $protoname.proto
  fi
done