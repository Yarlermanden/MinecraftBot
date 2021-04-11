import minerl

minerl.data.download('./data')
data = minerl.data.make('MineRLObtainDiamond-v0', data_dir='./data')

for current_state, action, reward, next_state, done in data.sarsd_iter(num_epochs=1, max_sequence_len=32):
    print(current_state['pov'][0])

    print(reward[-1])
    print(done[-1])
    print("at the end of trajectories the length can be < max_sequence_len", len(reward))

#export MINERL_DATA_ROOT='./data'
