import matplotlib.pyplot as plt

# Path to your data file
file_path = "D:/loss/train2.4.1.txt"

# Initialize lists to store the loss values
loss_values = []
epochs = []

# Open the file and read the lines
with open(file_path, 'r') as file:
    for line in file:
        parts = line.strip().split(', ')
        epoch_info, loss_info = parts[0], parts[1]
        epoch = int(epoch_info.split('=')[1].split('/')[0])
        loss = float(loss_info.split('=')[1])

        epochs.append(epoch)
        loss_values.append(loss)


# Plotting the loss values
plt.figure(figsize=(10, 6))
plt.plot(loss_values, label='Loss', color='blue')

# Add vertical lines and labels for each new epoch
current_epoch = 0
for i, epoch in enumerate(epochs):
    if epoch > current_epoch:
        plt.axvline(x=i+1, color='grey', linestyle='--', linewidth=0.5)
        plt.text(i+1, plt.ylim()[1], f'Epoch {epoch}', fontsize=8, rotation=90)
        current_epoch = epoch

plt.xlabel('Iteration')
plt.ylabel('Loss')
plt.title('Loss during the whole training')
plt.legend()
plt.grid(True)
plt.show()